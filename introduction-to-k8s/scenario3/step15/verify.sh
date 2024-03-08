#!/bin/bash

# Check container image used
container_id=$(docker ps --filter "ancestor=ubuntu" --format "{{.ID}}")

if [ -z "$container_id" ]; then
    echo "No container is running from ubuntu image"
    exit 1
fi

# Invoke Python script to check container conf
python3 /my/location/check_step15.py $container_id
exit_code=$?

exit $exit_code