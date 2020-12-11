#!/bin/bash

source ./scripts/helpers.sh

# Check if pip3 is installed
pip3 --version > /dev/null 2>&1
if [[ $? -ne 0 ]]
then
    printf "\nPlease install pip:\n[ https://pip.pypa.io/en/stable/installing/# ]\n";
    exit 0;
fi

# Check if pipenv is installed
pipenv --version > /dev/null 2>&1
if [[ $? -ne 0 ]]
then
    pip3 install pipenv;
fi

# Check if Pipfile exists
if [ ! -f "Pipfile" ]; then
    echo "Pipfile does not exist.";
fi

# Check if Pipfile.lock exists
if [ ! -f "Pipfile.lock" ]; then
    pipenv lock
fi

pipenv sync --dev;
