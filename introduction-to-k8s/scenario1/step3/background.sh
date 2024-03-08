#!/bin/bash

kubectl create deployment newpods --image busybox --replicas 2 -- sleep 1000

echo done > /tmp/background_step3