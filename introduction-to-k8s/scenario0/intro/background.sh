#!/bin/sh

kubectl create deployment lab-dep --image nginx:latest --replicas 2

echo done > /tmp/background_intro