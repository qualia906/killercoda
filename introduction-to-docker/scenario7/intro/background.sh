#!/bin/bash

docker network create --driver bridge --subnet 182.18.0.1/24 --gateway 182.18.0.1 lab-network
mkdir /root/click-counter

echo done > /tmp/background_intro