#!/bin/bash

# nginx-2 Pod 内で /data/mydata.txt の内容を取得
file_content=$(kubectl exec nginx-2 -- cat /data/mydata.txt)

# ファイルの内容が期待通りか確認
if [ "$file_content" == "my_data" ]; then
    echo "ファイルの内容が正しいです。"
    exit 0
else
    echo "ファイルの内容が期待と異なります。"
    exit 1
fi
