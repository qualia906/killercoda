#!/bin/bash
docker ps | grep redis
if [ $? -eq 0 ]; then
  echo "done"
else
  echo "Failure"
fi