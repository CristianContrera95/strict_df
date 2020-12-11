# StrictDataFrame
*********************

The Pandas DataFrames can handle mixed data types on the columns: for instance, a column "month" can have both integer and string values, being "object" the data type associated in those cases. This ability could result in undesired side effects in several use cases, especially on data pipelines where it is necessary to know the type of data processed over the steps.


This is a library that provides utils to handle Pandas DataFrames in a "strict" way regarding the data schema, so a DataFrame enforces a proper data type for each of its columns, as well as other related utils.

---
## Quickstart

### Installation

Installing **strictdf** is done in the usual ways. The simplest way is with pip:

``` bash
pip install git+git://github.com/CristianContrera95/strict_df.git
```

- Note:  
    It is **very** important to install **strictdf** on the *correct* version of
    Python. StrictDataFrame requires *Python>=3.9*.

### Using stricdf
To start using **stricdf**, open an jupyter or ipython sheel and run:
``` python
from strictdf import StrictDataFrame

df = pd.read_csv('data.csv')

sdf = StrictDataFrame(df)

sdf.dtypes
# {'serious_dlqin2yrs': 'bool',
#  'revolving_utilization_of_unsecured_lines': 'float64',
#  'age': 'int64',
#  'number_of_time30-59_days_past_due_not_worse': 'int64',
#  'debt_ratio': 'float64',
#  'monthly_income': 'int64'
# }

sdf.report()
# "DataFrame having shape '(120157, 11)' (29843 rows removed from original)"
```

---

## API

This part of the documentation covers all the interfaces of **strictdf**  


### StrictDataFrame

The StrictDataFrame class implements strict dtypes for DataFrames columns

**StrictDataFrame**(*df*, *min_percentage*: Union[int, float] = 90, *impute*: bool = False, *binary2bool*: bool = False, *skip_col*: Union[List, np.array] = None)
``` python
from strictdf import StrictDataFrame
```
StrictDataFrame is a pd.DataFrame wrapper that provides utilities to handle in a "strict" DataFrames
    way with respect to the data schema, so it imposes a suitable data type for each of its columns

##### Parameters

- **df** : pandas DataFrame
    Contains data stored in DataFrame.

- **min_percentage** : int or float optional (default=.90)
    Values must be between 0 and 100 or 0. and 1. (if float if given)
    Used to determine the type of a column, requires 'min_percentage' of rows to be 1 expected type

- **impute** : bool optional (default=False)

- **binary2bool** : bool optional (default=False)

##### Attributes
- **old_df** : pd.DataFrame
    Original pd.DataFrame given

- **new_df** : pd.DataFrame
    Modified pd.DataFrame with "strict" types for each column

- **impute** : bool (default=False)
    Impute values that are being removed to not meet expected data types.
    For columns float 'mean' is used, for integer 'mode' is used

- **binary2bool** : bool (default=False)
    Convert all columns with only 2 values to boolean

- **skip_col** : list or array-like
    Column names to be omitted

##### Methods

- **report()** : Prints current df's shape and diff with original df


### Utils
The module provides common functions used in several code parts

### Utils.dtypes

This module implements function to infer data types

##### Functions

- **str_check_bool(*string*)** : Check if given string is bool
- **str_check_int(*string*)** : Check if given string is int
- **str_check_float(*string*)** : Check if given string is float

#### dataset
This module only for develops purposes

##### Function

- **load_credit_data()**: Allow a download csv file to test StrictDataFrame

---
