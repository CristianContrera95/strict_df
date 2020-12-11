#!/bin/bash

# get dir of current script
CUR_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
# cd to project root
cd "$CUR_DIR/.."

generate_requirements() {
    pipfile2req > requirements.txt;
    pipfile2req --dev > requirements-dev.txt;
}

remove_requirements() {
    rm requirements*.txt;
}
