#!/bin/bash

container_id=$(docker ps --filter "name=mysql-db" --format "{{.ID}}")

if [ -z "$container_id" ]; then
    exit 1
fi

python3 /my/location/check_step11.py $container_id
exit_code=$?

exit $exit_code
