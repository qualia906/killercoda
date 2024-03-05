#!/bin/bash

# Verify container image
container_id=$(docker ps --filter "ancestor=qualia906/simple-webapp:blue" --format "{{.ID}}")

if [ -z "$container_id" ]; then
    exit 1
fi

# Invoke Python script to check port configuration and detached mode
python3 /my/location/check_step6.py $container_id
exit_code=$?

exit $exit_code
