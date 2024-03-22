#!/bin/bash

kubectl create deployment backend-redis --image=redis --port=6379 --replicas=1

echo "done" > /tmp/background_step6