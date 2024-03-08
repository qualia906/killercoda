#!/bin/bash

# コンテナ名を指定
container_name="alpine-2"

# コンテナが存在するかどうかをチェック
if ! docker ps -a --format "{{.Names}}" | grep -q "^${container_name}$"; then
    echo "Container ${container_name} does not exist."
    exit 1
fi

# Pythonスクリプトを使用して、コンテナの設定を詳細にチェック
python3 /my/location/check_step4.py "$container_name"
