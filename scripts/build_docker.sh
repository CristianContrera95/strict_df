#!/bin/bash

# get dir of current script
CUR_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
# cd to project root
cd "$CUR_DIR/.."

pipenv lock --requirements > requirements.txt
pipenv lock --requirements --dev > requirements-dev.txt

docker build -t strict_df_test .

rm requirements*.txt
