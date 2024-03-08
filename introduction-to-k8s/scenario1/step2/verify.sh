#!/bin/bash

# 指定された Pod 名とイメージを変数に格納
POD_NAME="nginx-1"
IMAGE_NAME="nginx"

# kubectl コマンドを使用して、指定された Pod の情報を取得
POD_INFO=$(kubectl get pods --output=jsonpath='{.items[?(@.metadata.name=="'$POD_NAME'")]}')

# Pod が存在するか確認
if [ -z "$POD_INFO" ]; then
  echo "Pod $POD_NAME が見つかりません。"
  exit 1
fi

# 使用されているイメージを確認
POD_IMAGE=$(kubectl get pod $POD_NAME -o jsonpath='{.spec.containers[*].image}')

if [ "$POD_IMAGE" == "$IMAGE_NAME" ]; then
  echo "コマンドが正しく実行されました。"
  exit 0
else
  echo "Pod $POD_NAME は存在しますが、イメージ名が $IMAGE_NAME と一致しません。"
  exit 1
fi
