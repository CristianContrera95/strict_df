#!/bin/bash
source ./scripts/helpers.sh

generate_requirements

rm -r build/ > /dev/null 2>&1 &&  rm -r dist/ > /dev/null 2>&1

python setup.py bdist_wheel
python setup.py clean

remove_requirements
