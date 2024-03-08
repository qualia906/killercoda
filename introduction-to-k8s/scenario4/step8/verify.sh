#!/bin/bash

# コンテナ名を指定
container_name="my-registry"

# 実行中のコンテナリストと停止中のコンテナリストの両方でコンテナ名を検索
container_running=$(docker ps --filter "name=$container_name" --format "{{.Names}}")
container_stopped=$(docker ps -a --filter "name=$container_name" --format "{{.Names}}")

if [ -z "$container_running" ] && [ -z "$container_stopped" ]; then
    echo "Container ${container_name} has been removed."
    exit 0
else
    echo "Container ${container_name} has not been removed."
    exit 1
fi
