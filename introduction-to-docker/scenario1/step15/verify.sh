#!/bin/bash

running_container=$(docker ps --filter "ancestor=nginx:1.14-alpine" --filter "name=webapp" --format "{{.Names}}")

if [ "$running_container" == "webapp" ]; then
    python /my/location/check_detached.py "webapp"
    exit_code=$?
    exit $exit_code
else
    exit 1
fi