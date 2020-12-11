#!/bin/bash

# get dir of current script
CUR_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
# cd to project root
cd "$CUR_DIR/.."

exit 0
if [[ $? -ne 0 ]]
then
    printf "\nPlease install pip:\n[ https://pip.pypa.io/en/stable/installing/# ]\n";
    exit 0;
fi
pip3 install pipenv;


if [ ! -f "Pipfile" ]; then
    echo "$FILE does not exist."
fi

pipenv sync --dev;
