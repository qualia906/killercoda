#!/bin/bash

# Verify that the container image nginx:1.14-alpine was pulled and isavailable locally.
docker images | grep nginx | grep 1.14-alpine
if [ $? -eq 0 ]; then
  exit 0
fi
exit 1
