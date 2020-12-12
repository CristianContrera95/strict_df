"""
StrictDataFrame
---------------
A pd.DataFrame wrapper that provides utilities to handle in a "strict" DataFrames way with respect to the data schema
"""

import pandas as pd
import numpy as np
from pyspark.sql import SparkSession
from copy import copy
from typing import Union, List
from .utils.dtypes import str_check_bool, str_check_int, str_check_float


class StrictDataFrame():
    """
    StrictDataFrame is a pd.DataFrame wrapper that provides utilities to handle in a "strict" DataFrames
    way with respect to the data schema, so it imposes a suitable data type for each of its columns

    Parameters
    ----------
    df : pandas DataFrame
        Contains data stored in DataFrame.

    min_percentage : int or float optional (default=.90)
        Values must be between 0 and 100 or 0. and 1. (if float if given)
        Used to determine the type of a column, requires 'min_percentage' of rows to be 1 expected type

    impute : bool optional (default=False)

    binary2bool : bool optional (default=False)

    Attributes
    ----------
    old_df : pd.DataFrame
        Original pd.DataFrame given

    new_df : pd.DataFrame
        Modified pd.DataFrame with "strict" types for each column

    impute : bool (default=False)
        Impute values that are being removed to not meet expected data types.
        For columns float 'mean' is used, for integer 'mode' is used

    binary2bool : bool (default=False)
        Convert all columns with only 2 values to boolean

    skip_col : list or array-like
        Column names to be omitted

    Examples
    --------
    from strictdf import StrictDataFrame
    import pandas as pd

    df = pd.read_csv("data/credit-data.csv")

    sdf = StrictDataFrame(df)

    Notes
    -----
    - NaNs values are dropped before data types inference.

    """

    def __init__(self, df, min_percentage: Union[int, float] = 90, impute: bool = False,
                 binary2bool: bool = False, skip_col: Union[List, np.array] = None):

        assert isinstance(df, pd.DataFrame), '"df" param must be a pd.DataFrame'
        assert isinstance(min_percentage, float) or \
               isinstance(min_percentage, int), '"min_percentage" param must be float or int'

        self.impute = impute
        self.binary2bool = binary2bool
        self.skip_col = [] if skip_col is None else skip_col
        self.min_percentage = min_percentage
        if isinstance(self.min_percentage, float):
            self.min_percentage *= 100

        self.old_df = copy(df)
        if not df.empty:
            self.new_df = self.__strict_df(copy(self.old_df))
        else:
            self.new_df = copy(df)

    @property
    def dtypes(self) -> dict:
        # change type object to str (why? there's doesn't why..)
        return {a: (b.name if b.name != 'object' else 'str')
                for a, b in self.new_df.dtypes.items()}

    def __strict_df(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Function to infer the types of each column
        """
        df.dropna(inplace=True)

        if self.binary2bool:
            def __binary2bool(col):
                return (col - col.unique().max()).astype(bool) if len(col.unique()) == 2 else col

            df = df.apply(__binary2bool)

        cols_mask = df.columns.difference(self.skip_col)
        columns = df[cols_mask].select_dtypes(exclude=['bool']).columns

        # Drop all rows with unexpected value for given column
        unexpected_mask = np.ones(len(df), dtype=bool)
        for col in columns:
            _mask = df[col].map(lambda x: bool(str_check_bool(str(x))) or
                                bool(str_check_int(str(x))) or bool(str_check_float(str(x)))
                                ).values
            if sum(~_mask) / len(_mask) * 100 < (100 - self.min_percentage):
                # Columns with more than '1-min_percentage' values
                unexpected_mask &= _mask
        df.drop(df[~unexpected_mask].index, inplace=True)

        # over each expected column infer dtype and cast it
        for col in columns:
            type_mask = df[col].map(lambda x: bool(str_check_bool(str(x))))
            if all(type_mask):
                # all values are booleans
                df[col] = df[col].astype(bool)
            else:
                type_mask = df[col].map(lambda x: bool(str_check_int(str(x))))
                if sum(type_mask) / len(type_mask) * 100 >= self.min_percentage:
                    # min_percentage values are int
                    df = self.__handle_unexpected_values(df, type_mask, col, 'int')
                    df.loc[:, col] = df[col].astype(float).astype(np.int64)
                else:
                    type_mask = df[col].map(lambda x: bool(str_check_float(str(x))))
                    if sum(type_mask) / len(type_mask) * 100 >= self.min_percentage:
                        # min_percentage values are float
                        df = self.__handle_unexpected_values(df, type_mask, col, 'float')
                        df.loc[:, col] = df[col].astype(float)
        return df

    def __handle_unexpected_values(self, df, type_mask, col, dtype):
        if self.impute:
            return self.__impute_values(df, type_mask, col, dtype)
        return df.drop(df[~type_mask].index)

    def __impute_values(self, df, type_mask, col, dtype):
        if dtype == 'int':
            df.loc[df[~type_mask].index, col] = df[col].mode()
        if dtype == 'float':
            df.loc[df[~type_mask].index, col] = df[col].mean()
        return df

    def report(self) -> str:
        """
        Returns shape of new and old DataFrames
        """
        rows_diff = self.old_df.shape[0] - self.new_df.shape[0]
        text = f"DataFrame having shape '{self.new_df.shape}' ({rows_diff} rows removed from original)"
        return text

    def to_spark(self):
        spark = SparkSession.builder.getOrCreate()
        return spark.createDataFrame(self.new_df)
