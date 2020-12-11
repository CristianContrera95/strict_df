# Strict DataFrame


### Motivation:

The Pandas DataFrames can handle mixed data types on the columns: for instance, a column "month" can have both integer and string values, being "object" the data type associated in those cases. This ability could result in undesired side effects in several use cases, especially on data pipelines where it is necessary to know the type of data processed over the steps.


This is a library that provides utils to handle Pandas DataFrames in a "strict" way regarding the data schema, so a DataFrame enforces a proper data type for each of its columns, as well as other related utils.

### Installation

#### Prerequisites:
For use strictdf, install before:
- python>=3.9
- pip

And need a bash console

- Note:  
    **If you are using windows os, you are starting very very bad**.   
    Anyway *library_create.bat* for windows is provided.  
    But you shouldn't program on that OS

With prerequisites ready you can run:

``` bash
chmod +x script/*
./script/create_env.sh
./library_create.sh
```


#### And the you can install strictdf where you want to use it! 

