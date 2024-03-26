#!/bin/bash

# Pod の詳細を取得
output=$(kubectl get pod pod-emptydir -o json)

# Python スクリプトに出力を渡して解析し、Python スクリプトの終了コードを変数に格納
python3 /my/location/check_step1.py "$output"
result=$?

# Python スクリプトの終了コードに基づいてシェルスクリプトの終了コードを設定
if [ $result -eq 0 ]; then
    echo "Pod 'pod-emptydir' は正しく設定されています。"
    exit 0
else
    echo "Pod 'pod-emptydir' の設定に問題があります。"
    exit 1
fi
