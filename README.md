# Strict DataFrame


### Motivation:

The Pandas DataFrames can handle mixed data types on the columns: for instance, a column "month" can have both integer and string values, being "object" the data type associated in those cases. This ability could result in undesired side effects in several use cases, especially on data pipelines where it is necessary to know the type of data processed over the steps.


This is a library that provides utils to handle Pandas DataFrames in a "strict" way regarding the data schema, so a DataFrame enforces a proper data type for each of its columns, as well as other related utils.

### Setup

