#!/bin/bash

# Specify container name and tag
container_name="my-registry"
image_name="registry:2"

# Check container name and image used
container_id=$(docker ps --filter "name=$container_name" --filter "ancestor=$image_name" --format "{{.ID}}")

if [ -z "$container_id" ]; then
    echo "Container is not running"
    exit 1
fi

# Invoke Python script to check container conf
python3 /my/location/check_step4.py "$container_id"
exit_code=$?

exit $exit_code
