#!/bin/bash

# ネットワーク名を指定
network_name="mysql-network"

# ネットワークが存在するかどうかをチェック
if ! docker network ls --format "{{.Name}}" | grep -q "^${network_name}$"; then
    echo "Network ${network_name} does not exist."
    exit 1
fi

# Pythonスクリプトを使用して、ネットワークの詳細設定をチェック
python3 /my/location/check_step5.py "$network_name"
