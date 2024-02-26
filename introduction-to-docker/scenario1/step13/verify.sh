#!/bin/bash
# Verify that ubuntu image has been deleted.
docker images | grep ubuntu
if [ $? -eq 0 ]; then
  exit 1
fi
exit 0
