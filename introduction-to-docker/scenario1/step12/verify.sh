#!/bin/bash
# Verify that all containers that are running and stopped are deleted.
docker ps -a | grep -v "CONTAINER ID"
if [ $? -eq 0 ]; then
  exit 1
fi
exit 0
