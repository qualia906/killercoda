#!/bin/bash

kubectl apply -f /root/manifests/frontend-deployment.yaml
kubectl apply -f /root/manifests/frontend-service.yaml

echo "done" > /tmp/background_intro