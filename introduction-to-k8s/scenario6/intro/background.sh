#!/bin/sh

docker container run -d --name alpine-1 alpine sleep 1000

echo done > /tmp/background_intro