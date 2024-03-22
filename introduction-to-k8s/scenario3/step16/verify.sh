#!/bin/bash

# Namespace の一覧を取得して特定の Namespace が存在するか確認
kubectl get namespace dev --no-headers &> /dev/null

# 前のコマンドの終了コードに基づいて判断
if [ $? -eq 0 ]; then
    echo "Namespace 'dev' が正しく作成されました。"
    exit 0
else
    echo "Namespace 'dev' が見つかりません。"
    exit 1
fi
