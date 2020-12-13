#!/bin/bash
source ./scripts/helpers.sh

generate_requirements

rm -r build/ > /dev/null 2>&1 &&  rm -r dist/ > /dev/null 2>&1

pipenv run python setup.py bdist_wheel
pipenv run python setup.py clean

remove_requirements
