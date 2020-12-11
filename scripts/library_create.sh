#!/bin/bash

# get dir of current script
CUR_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
# cd to project root
cd "$CUR_DIR/.."

python3 setup.py sdist --format=zip
