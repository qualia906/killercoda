#!/bin/bash

# Pythonスクリプトを使用して、nginxとhttpdイメージがローカルレジストリに存在するかチェック
python3 /my/location/check_step5.py "localhost:5000/nginx" "localhost:5000/httpd"

exit_code=$?

if [ $exit_code -eq 0 ]; then
    echo "All specified images are stored."
else
    echo "All specified images are not stored."
fi

exit $exit_code
