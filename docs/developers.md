# StrictDataFrame
*********************

The Pandas DataFrames can handle mixed data types on the columns: for instance, a column "month" can have both integer and string values, being "object" the data type associated in those cases. This ability could result in undesired side effects in several use cases, especially on data pipelines where it is necessary to know the type of data processed over the steps.


This is a library that provides utils to handle Pandas DataFrames in a "strict" way regarding the data schema, so a DataFrame enforces a proper data type for each of its columns, as well as other related utils.

---
## Developers guide

### Installing dev mode

Installing **strictdf** dev mode is done in the usual ways.

#### Github

You can download the project from github repository and create a distribution wheel from code.
Open a bash shell in the root of project and run:

``` bash
chmod +x script/library_create.sh
./script/library_create.sh
```

- **if you are using windows os, you are starting very very bad.** Anyway `library_create.bat` for windows is provided.

Those commands should create two folders *build* and *dist*

Now can install with pip following:
``` bash
pip install dist/strictdf-0.1.0-py3-none-any.whl
```

- Note:  
    It is **very** important to install **strictdf** on the *correct* version of
    Python. StrictDataFrame requires *Python>=3.9*.

- Note:  
    Install **strictdf** on dev mode allow run test and check coverage.


### Run Tests

To run test, You must download **strictdf** from github (previous section) and follow one of the following paths 

#### Docker 

Using Dockerfile provided, You can build docker image, it's very easy, only open a bash shell and run:

``` bash
chmod +x script/build_docker.sh
./script/build_docker.sh
```
And when this ends:

``` bash
docker run -it strict_df_test
```

#### Hands

With a shell in the root of the project, run:
``` bash
chmod +x script/create_env.sh
chmod +x script/run_test.sh

create_env.sh
run_test.sh
```

- Note:
    To perform this, you need install **python3.9** with [pyenv](https://github.com/pyenv/pyenv)
    and pip for that python version.