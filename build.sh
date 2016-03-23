#!/usr/bin/env bash

set -x -e

docker build -t haproxy haproxy/
docker build -t journals journals/
docker build -t autocomplete autocomplete/
