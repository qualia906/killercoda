#!/bin/bash

# ファイルパスを指定
compose_file="/root/click-counter/docker-compose.yml"

# docker-compose.ymlファイルが存在するかチェック
if [ ! -f "$compose_file" ]; then
    echo "${compose_file} does not exist."
    exit 1
fi

# Pythonスクリプトを使用して、ファイル内容を詳細にチェック
python3 /my/location/check_step5.py "$compose_file"
