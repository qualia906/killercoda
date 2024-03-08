#!/bin/bash

# Pod名とイメージ名を変数に設定
POD_NAME="redis"
IMAGE_NAME="redis:alpine"

# 指定されたPodの情報を取得
POD_INFO=$(kubectl get pods --output=jsonpath='{.items[?(@.metadata.name=="'$POD_NAME'")].spec.containers[*].image}')

# Podが存在し、イメージが期待通りかチェック
if [[ "$POD_INFO" == *"$IMAGE_NAME"* ]]; then
  echo "Command was executed successfully."
  exit 0
else
  echo "Command was not executed or Pod/Image does not match."
  exit 1
fi
