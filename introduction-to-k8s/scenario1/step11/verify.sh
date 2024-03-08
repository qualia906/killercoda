#!/bin/bash

POD_NAME="webapp"

# Kubernetes クラスターで指定された Pod が存在するか確認
kubectl get pod $POD_NAME &> /dev/null

# $? は直前のコマンドの終了ステータスを保持
if [ $? -eq 0 ]; then
    # Pod が存在する場合、終了コード 1 を返して終了
    echo "Pod $POD_NAME still exists."
    exit 1
else
    # Pod が存在しない場合、終了コード 0 を返して終了
    echo "Pod $POD_NAME does not exist. Command was likely executed."
    exit 0
fi
