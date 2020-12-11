import pytest
import pandas as pd
import numpy as np
from src.strictdf import StrictDataFrame


@pytest.mark.parametrize(
    'df, expected',
    [
        (pd.DataFrame({}), pd.DataFrame({})),

        (pd.DataFrame({
            'col1': np.arange(10),
            'col2': list(range(9)) + ['none'],
            'col3': list(map(float, range(9))) + ['none'],
            'col4': list(map(bool, range(9))) + ['none'],
            'col5': map(bool, range(10)),
            'col6': list(map(str, range(9))) + ['none'],
        }),
         pd.DataFrame({
            'col1': np.arange(10),
            'col2': list(range(9)) + ['none'],
            'col3': list(map(float, range(9))) + ['none'],
            'col4': list(map(bool, range(9))) + ['none'],
            'col5': map(bool, range(10)),
            'col6': list(map(str, range(9))) + ['none'],
        })
        ),
    ]
)
def test_old_df(df, expected):
    sdf = StrictDataFrame(df)

    assert sdf.old_df.shape[0] == df.shape[0]
    assert pd.concat([sdf.old_df, expected]).drop_duplicates(keep=False).shape[0] == 0


@pytest.mark.parametrize(
    'df, expected',
    [
        (pd.DataFrame({}), pd.DataFrame({})),

        (pd.DataFrame({
            'col1': np.arange(10),
            'col2': list(range(9)) + ['none'],
            'col3': list(map(float, range(9))) + ['none'],
            'col4': list(map(bool, range(9))) + ['none'],
            'col5': map(bool, range(10)),
            'col6': list(map(str, range(9))) + ['none'],
        }),
         pd.DataFrame({
            'col1': np.arange(9),
            'col2': np.arange(9),
            'col3': np.arange(9),
            'col4': map(bool, range(9)),
            'col5': map(bool, range(9)),
            'col6': np.arange(9),
        }),
        ),
    ]
)
def test_new_df(df, expected):
    sdf = StrictDataFrame(df)

    assert sdf.new_df.shape[0] <= df.shape[0]
    assert pd.concat([sdf.new_df, expected]).drop_duplicates(keep=False).shape[0] == 0


@pytest.mark.parametrize(
    'df, expected',
    [
        (pd.DataFrame({
            'col1': np.arange(10),
            'col2': list(range(9)) + ['none'],
            'col3': list(map(float, range(9))) + ['none'],
            'col4': list(map(bool, range(9))) + ['none'],
            'col5': map(bool, range(10)),
            'col6': list(map(str, range(9))) + ['none'],
        }),
         {  'col1': 'int64',
            'col2': 'int64',
            'col3': 'int64',
            'col4': 'bool',
            'col5': 'bool',
            'col6': 'int64',
            }
        ),

        (pd.DataFrame({
            'col1': ['1.5' for _ in range(9)] + ['none'],
            'col2': ['1.5' for _ in range(5)] + ['1.0' for _ in range(5)],
            'col3': ['1.5' for _ in range(9)] + [np.nan],
            'col4': ['a' for _ in range(10)],
        }),
         {  'col1': 'float64',
            'col2': 'float64',
            'col3': 'float64',
            'col4': 'str',
            }
        ),
    ]
)
def test_new_df_dtypes(df, expected):
    sdf = StrictDataFrame(df)

    assert sdf.dtypes == expected


@pytest.mark.parametrize(
    'df, expected',
    [
        (pd.DataFrame({
            'col1': np.arange(10),
            'col2': list(range(9)) + ['none'],
            'col3': list(map(float, range(9))) + ['none'],
            'col4': list(map(bool, range(9))) + ['none'],
            'col5': map(bool, range(10)),
            'col6': list(map(str, range(9))) + ['none'],
        }),
         "DataFrame having shape '(9, 6)' (1 rows removed from original)"
        ),

        (pd.DataFrame({
            'col1': ['1.5' for _ in range(9)] + ['none'],
            'col2': ['1.5' for _ in range(5)] + ['1.0' for _ in range(5)],
            'col3': ['1.5' for _ in range(9)] + [np.nan],
            'col4': ['a' for _ in range(10)],
        }),
         "DataFrame having shape '(9, 4)' (1 rows removed from original)"
        ),
    ]
)
def test_report(df, expected):
    sdf = StrictDataFrame(df)

    assert sdf.report() == expected
