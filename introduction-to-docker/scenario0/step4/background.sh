#!/bin/sh

docker container run -d --name alpine-1 alpine sleep 300

echo done > /tmp/background_step4