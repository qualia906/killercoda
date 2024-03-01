#!/bin/bash

# Set image name
image_name="color-webapp:lite"

# Check image name and tag
image_info=$(docker images --format "{{.Repository}}:{{.Tag}} {{.Size}}" | grep "^${image_name} ")
if [ -z "$image_info" ]; then
    exit 1
fi

# Check image size
image_size=$(echo $image_info | awk '{print $2$3}')
max_size="150MB"

if [ $(echo $image_size | grep -Eo '[0-9]+') -gt $(echo $max_size | grep -Eo '[0-9]+') ]; then
    exit 1
fi

# Invoke Python script to check image conf
python3 /my/location/check_step13.py $image_name
exit_code=$?

exit $exit_code
