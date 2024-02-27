#!/bin/bash

docker image pull redis
docker image pull nginx
docker image pull nginx:alpine
docker image pull mysql
docker image pull postgres
docker image pull alpine
docker image pull ubuntu
docker image pull kodekloud/simple-webapp-mysql
docker image pull kodekloud/simple-webapp

echo done > /tmp/background_intro