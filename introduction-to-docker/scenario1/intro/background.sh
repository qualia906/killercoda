#!/bin/bash

docker image pull redis
docker image pull nginx
docker image pull nginx:alpine
docker image pull alpine
docker image pull ubuntu

echo done > /tmp/background_intro