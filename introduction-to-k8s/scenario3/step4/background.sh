#!/bin/bash

kubectl create deployment frontend-dep --image busybox999 --replicas 4

echo "done" > /tmp/background_step4