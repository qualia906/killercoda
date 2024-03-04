#!/bin/bash

# ボリューム名を指定
volume_name="my-volume"

# Dockerボリュームリストに指定されたボリュームが存在するか確認
if docker volume ls --format "{{.Name}}" | grep -q "^${volume_name}$"; then
    echo "Volume ${volume_name} has been created."
    exit 0
else
    echo "Volume ${volume_name} has not been created."
    exit 1
fi
