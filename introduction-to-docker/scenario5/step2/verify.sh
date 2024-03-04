#!/bin/bash

# Specify the container name
container_name="alpine-1"

# Check if the container is running
if ! docker ps --format "{{.Names}}" | grep -q "^${container_name}$"; then
    echo "Container ${container_name} is not running."
    exit 1
fi

# Check the container configuration
python3 /my/location/check_step2.py "$container_name"
exit_code=$?

exit $exit_code
