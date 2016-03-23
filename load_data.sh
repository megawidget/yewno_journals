#!/usr/bin/env bash

set -e -x

while read p; do
  curl -d "title=$p" ${1:-192.168.99.100}/v1/journals
done <dataset.txt
