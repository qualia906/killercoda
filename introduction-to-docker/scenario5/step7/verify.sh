#!/bin/bash

# コンテナ名を指定
container_name="alpine-1"

# 実行中のコンテナリストと停止中のコンテナリストの両方でコンテナ名を検索
container_exists=$(docker ps -a --format "{{.Names}}" | grep -q "^${container_name}$")

if [ $? -eq 0 ]; then
    echo "Container ${container_name} is still running"
    exit 1
else
    echo "Container ${container_name} is not running"
    exit 0
fi
