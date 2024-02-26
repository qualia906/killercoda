#!/bin/bash

# Verify that the container using the redis image is stopped.

docker ps | grep redis
if [ $? -eq 0 ]; then
  exit 1
fi
exit 0
