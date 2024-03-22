#!/bin/bash

kubectl create ns sales
kubectl create ns marketing
kubectl create ns finance
kubectl create ns prod
kubectl create ns research
kubectl create deployment lab-1 -n research --image nginx --replicas 2

echo done > /tmp/background_intro