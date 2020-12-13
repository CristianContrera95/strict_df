#!/bin/bash

source ./scripts/helpers.sh

active_env

generate_requirements

docker build -t strict_df_test .

remove_requirements