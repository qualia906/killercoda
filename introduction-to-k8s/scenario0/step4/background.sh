#!/bin/sh

kubectl run lab-pod --image redis

echo done > /tmp/background_step4