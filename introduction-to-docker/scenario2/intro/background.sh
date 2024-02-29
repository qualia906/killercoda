#!/bin/bash

docker container run -d -p 3456:3456 -p 38080:80 nginx-alpine

echo done > /tmp/background_intro