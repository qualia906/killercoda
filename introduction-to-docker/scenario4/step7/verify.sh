#!/bin/bash

# イメージ名を指定
image_name="localhost:5000/nginx"

# Dockerイメージリストに指定されたイメージが存在するか確認
image_exists=$(docker images --format "{{.Repository}}:{{.Tag}}" | grep "^${image_name}")

if [ -z "$image_exists" ]; then
    echo "Not exist: ${image_name}"
    exit 1
else
    echo "Exist: ${image_name}"
    exit 0
fi
