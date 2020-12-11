#!/bin/bash

source ./scripts/helpers.sh

coverage run -m pytest -v
coverage report
