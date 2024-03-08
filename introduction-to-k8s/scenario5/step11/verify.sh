#!/bin/bash

# コンテナ名とファイルパスを指定
container_name="nginx-1"
file_path="/usr/local/share/my-volume/data.txt"
expected_text="My important data"

# コンテナ内のファイルからテキストを読み取り、期待するテキストが含まれているか確認
if docker exec $container_name cat $file_path | grep -qF "$expected_text"; then
    echo "ファイルに期待するテキストが正しく書き込まれています。"
    exit 0
else
    echo "ファイルに期待するテキストが書き込まれていません。"
    exit 1
fi

