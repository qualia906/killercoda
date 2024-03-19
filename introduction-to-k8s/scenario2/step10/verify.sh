#!/bin/bash

# ファイル名を直接指定
file1="/my/location/answer10.yaml"
file2="/root/playbooks/question10.yaml"

# Pythonスクリプトを使用してYAMLファイルを比較
python /my/location/compare_yaml.py "$file1" "$file2"

# Pythonスクリプトの終了コードに基づいて処理
if [ "$?" -eq 0 ]; then
    echo "YAML files are equivalent."
    exit 0
else
    echo "YAML files are not equivalent."
    exit 1
fi