#!/usr/bin/env bash

#bash scripts/set_env.sh
#hrun testcases/test_student.yml --dot-env-path=.env-$1  ./run.sh test

hrun testsuites/test_shanxi.yml  --dot-env-path=.env-shanxi

python3 scripts/rename_reports.py
