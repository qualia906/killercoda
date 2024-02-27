#!/bin/bash

docker container run -d alpine sleep 3600
docker container run -d -p 80 --name nginx-1 nginx:alpine
docker container run -d -p 80 --name nginx-2 nginx:alpine
docker container run -d --name awesome_northcut ubuntu sleep 3600
docker container run -d redis
docker container run -d alpine

echo done > /tmp/background7