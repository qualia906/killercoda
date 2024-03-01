#!/bin/bash

# 現在ローカルに存在するすべてのDockerイメージのリストを取得し、Pythonスクリプトに渡す
docker images --format "{{.Repository}}:{{.Tag}}" | python3 /my/location/check_step6.py
