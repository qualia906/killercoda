#!/bin/bash

# Specify the image name
image_name="color-webapp"

# Search the specified image
image_info=$(docker images --format "{{.Repository}}:{{.Tag}} {{.ID}}" | grep "^${image_name}:")
if [ -z "$image_info" ]; then
    exit 1
fi

# Invoke script to check the image
python3 /my/location/check_step8.py "${image_name}"
exit_code=$?

exit $exit_code
