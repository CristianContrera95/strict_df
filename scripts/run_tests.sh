#!/bin/bash

# get dir of current script
CUR_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
# cd to project root
cd "$CUR_DIR/.."

coverage run -m pytest -v
coverage report
