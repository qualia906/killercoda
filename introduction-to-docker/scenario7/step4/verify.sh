#!/bin/bash

# コンテナ名を指定
containers=("redis" "clickcounter")

# すべてのコンテナに対してチェックを実行
for container_name in "${containers[@]}"; do
    if docker ps -a --format "{{.Names}}" | grep -q "^${container_name}$"; then
        echo "Container ${container_name} exists."
        exit 1
    fi
done

echo "All containers are deleted."
exit 0
