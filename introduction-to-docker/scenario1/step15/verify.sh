#!/bin/bash

# Verify that the container using image nginx:1.14-alpine is runnning and that that container is named webapp.
docker ps | grep nginx:1.14-alpine | grep webapp
if [ $? -eq 0 ]; then
  exit 0
fi
exit 1