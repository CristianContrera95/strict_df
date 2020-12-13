#!/bin/bash

source ./scripts/helpers.sh

active_env

pipenv run coverage run -m pytest -v
pipenv run coverage report
