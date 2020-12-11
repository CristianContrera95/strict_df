# Strict DataFrame


### Motivation:

The Pandas DataFrames can handle mixed data types on the columns: for instance, a column "month" can have both integer and string values, being "object" the data type associated in those cases. This ability could result in undesired side effects in several use cases, especially on data pipelines where it is necessary to know the type of data processed over the steps.


This is a library that provides utils to handle Pandas DataFrames in a "strict" way regarding the data schema, so a DataFrame enforces a proper data type for each of its columns, as well as other related utils.


### Read docs
Once cloned this project, only open a shell in the root of project and run:
``` bash
pip install mkdocs
mkdocs serve
```
And follow the link http://127.0.0.1:8000


### Installation

#### Prerequisites:
For use strictdf, install before:
- python>=3.9
- pip

***And need a bash console***

- **Note**:  
    **If you are using windows os, you are starting very very bad**.   
    Anyway *library_create.bat* for windows is provided.  
    But you shouldn't program on that OS

With prerequisites ready you can run:

``` bash
pip install git+git://github.com/CristianContrera95/strict_df.git
```

Or cloning this repository:

``` bash
chmod +x script/*
./script/create_env.sh
./library_create.sh
```

#### And then you can install strictdf where you want to use it! 

``` bash
pip install dist/strictdf-0.1.0-py3-none-any.whl
```
