#!/bin/bash

# コンテナ名を指定
container_name="mysql-db"

# コンテナが実行中かどうかをチェック
if ! docker ps --format "{{.Names}}" | grep -q "^${container_name}$"; then
    echo "Container ${container_name} is not running."
    exit 1
fi

# Pythonスクリプトを使用して、コンテナの詳細設定をチェック
python3 /my/location/check_step6.py "$container_name"
