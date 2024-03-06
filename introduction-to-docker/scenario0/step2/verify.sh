#!/bin/bash

# コンテナ名と期待されるイメージを指定
container_name="test-1"
expected_image="nginx:latest"

# Pythonスクリプトを使用してコンテナが期待されるイメージから実行されているかチェック
python3 /my/location/check_step2.py "$container_name" "$expected_image"

# Pythonスクリプトの終了コードに基づいてスクリプトの終了コードを設定
exit_code=$?
exit $exit_code
