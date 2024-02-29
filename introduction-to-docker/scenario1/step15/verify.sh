#!/bin/bash

# Get the container ID.
container_id=$(docker ps | grep nginx:1.14-alpine | grep webapp | awk '{print $1}')

# Check if the container is running.
if [ -z "$container_id" ]; then
  exit 1
fi

# Check if the container is in detached mode.
if [ "$(docker inspect -f '{{ .State.Running }}' $container_id)" != "true" ]; then
  exit 1
fi

exit 0

