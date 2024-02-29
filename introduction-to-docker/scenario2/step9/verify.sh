#!/bin/bash

# Verify that container is running and its name is green-app.
container_id=$(docker ps --filter "name=green-app" --format "{{.ID}}")

if [ -z "$container_id" ]; then
    exit 1
fi

# Invoke Python script to check port conf, env variable and image.
python3 /my/location/check_step9.py $container_id
exit_code=$?

exit $exit_code
