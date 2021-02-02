#!/bin/bash

source ./scripts/helpers.sh

# active_env

if [ ! -f "requirements.txt" ]; then
  generate_requirements
fi

docker build -t strict_df_test .

remove_requirements
