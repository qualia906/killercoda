#!/bin/bash

# 指定された Deployment の存在を確認
kubectl get deployment frontend-green &> /dev/null

# コマンドの終了コードを確認
if [ $? -eq 0 ]; then
    # Deployment が存在する場合、エラーメッセージを表示して終了コード 1 で終了
    echo "Deployment 'frontend' はまだ存在します。"
    exit 1
else
    # Deployment が存在しない場合、成功メッセージを表示して終了コード 0 で終了
    echo "Deployment 'frontend' は正しく削除されました。"
    exit 0
fi