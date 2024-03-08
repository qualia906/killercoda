#!/bin/bash

# コンテナ名を指定
container_name="nginx-2"

# コンテナが実行中かどうかをチェック
if ! docker ps --format "{{.Names}}" | grep -q "^${container_name}$"; then
    echo "Container ${container_name} is not running."
    exit 1
fi

# Pythonスクリプトを使用して、コンテナの設定を詳細にチェック
python3 /my/location/check_step10.py "$container_name"
