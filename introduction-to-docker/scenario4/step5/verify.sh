#!/bin/bash

# ローカルレジストリのURL
registry_url="localhost:5000"

# チェックするイメージ
images=("nginx" "httpd")

# イメージがレジストリに存在するか確認する関数
check_image_in_registry() {
    image=$1
    full_image_name="${registry_url}/${image}"
    
    # イメージリストを取得して指定されたイメージが存在するか確認
    if curl -s "http://${registry_url}/v2/${image}/tags/list" | grep -q "tags"; then
        echo "${full_image_name} is in the registry"
    else
        echo "${full_image_name} is not in the registry"
        return 1
    fi
}

# すべてのイメージに対してチェックを実行
for image in "${images[@]}"; do
    if ! check_image_in_registry $image; then
        exit 1
    fi
done

# すべてのイメージが存在する場合
echo "OK"
exit 0
