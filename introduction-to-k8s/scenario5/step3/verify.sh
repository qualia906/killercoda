#!/bin/bash

# コンテナ名を指定
container_name="alpine-1"
# ファイル名を指定
file_name="newfile.txt"

# コンテナ内でファイルが存在するか確認
if docker exec $container_name ls / | grep -q "^${file_name}$"; then
    echo "File ${file_name} is exist in container ${container_name} ."
    exit 0
else
    echo "File ${file_name} is not exist in container ${container_name} ."
    exit 1
fi
