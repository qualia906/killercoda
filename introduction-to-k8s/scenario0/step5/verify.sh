#!/bin/bash

# Deployment の詳細を取得
output=$(kubectl get deployment test-2 -o json)

# Python スクリプトに出力を渡して解析し、Python スクリプトの終了コードを変数に格納
python3 /my/location/check_step5.py "$output"
result=$?

# Python スクリプトの終了コードに基づいてシェルスクリプトの終了コードを設定
if [ $result -eq 0 ]; then
    echo "条件を満たしています。"
    exit 0
else
    echo "条件を満たしていません。"
    exit 1
fi
