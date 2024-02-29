#!/bin/bash

# Verify all container image have been deleted.
docker images | grep -v "REPOSITORY"
if [ $? -eq 0 ]; then
  exit 1
fi
exit 0
