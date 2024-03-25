#!/bin/bash

# Deployment の現在のレプリカ数を取得
replicas=$(kubectl get deployment frontend-canary -o jsonpath='{.spec.replicas}')

# レプリカ数が期待値に一致するか確認
if [ "$replicas" -eq 4 ]; then
    # レプリカ数が4であれば、成功メッセージを表示して終了コード 0 で終了
    echo "Deployment 'frontend-canary' のレプリカ数は正しく4に設定されています。"
    exit 0
else
    # レプリカ数が4ではなければ、エラーメッセージを表示して終了コード 1 で終了
    echo "Deployment 'frontend-canary' のレプリカ数が期待値と一致しません。"
    exit 1
fi
