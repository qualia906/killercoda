#!/bin/bash

# コンテナ名と設定を指定
declare -A containers
containers[redis]="redis:alpine"
containers[clickcounter]="qualia906/click-counter"

# コンテナが実行中かどうか、および設定が正しいかをチェック
for container_name in "${!containers[@]}"; do
    if ! docker ps --format "{{.Names}}" | grep -q "^${container_name}$"; then
        echo "Container ${container_name} is not running"
        exit 1
    fi
done

# Pythonスクリプトを使用して、コンテナの設定を詳細にチェック
python3 /my/location/check_step6.py "${!containers[@]}"
