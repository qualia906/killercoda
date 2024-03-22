#!/bin/bash

# Deployment の詳細を取得
deployment_output=$(kubectl get deployment httpd-frontend -o custom-columns=NAME:.metadata.name,IMAGE:.spec.template.spec.containers[*].image,REPLICAS:.spec.replicas --no-headers)

# 関連する Pod の状態を取得
pods_output=$(kubectl get pods -l name=httpd-frontend -o custom-columns=NAME:.metadata.name,STATUS:.status.phase --no-headers)

# Python スクリプトに出力を渡して解析し、Python スクリプトの終了コードを変数に格納
python3 /my/location/check_step12.py "$deployment_output" "$pods_output"
result=$?

# Python スクリプトの終了コードに基づいてシェルスクリプトの終了コードを設定
if [ $result -eq 0 ]; then
    echo "条件を満たしています。"
    exit 0
else
    echo "条件を満たしていません。"
    exit 1
fi
