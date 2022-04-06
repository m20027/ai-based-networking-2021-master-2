#!/usr/bin/env bash

set -Ceuo pipefail

function error_handler() {
  set +x
  echo "something went wrong" >&2
  exit 1
}

: "start" && {
  echo "start..."
  trap error_handler ERR
  if [ ! -d logs ]; then
    mkdir logs
  fi
  if [ -e logs/result.txt ]; then
    rm logs/result.txt
    touch logs/result.txt
  fi
}

: "test" && {
  echo "testing..."
  KFOLD=5
  INPUT_DIR=sdataset_and_issue/dataset/original
  for i in `seq 0 9`
  do
    for k in `seq 1 ${KFOLD}`
    do
      python3 src/estimation.py -i ${INPUT_DIR}/{i}.json --model-path models/fold${k}_1000.mdl --test
    done
  done
}
: "aggregation" && {
  python3 src/aggregation.py
}

: "done" && {
  set +x
  echo "successful"
}
