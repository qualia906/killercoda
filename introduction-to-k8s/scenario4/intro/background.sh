#!/bin/bash

kubectl create deployment webapp --image qualia906/simple-webapp:red --replicas 4

echo "done" > /tmp/background_intro