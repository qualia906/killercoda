#!/bin/bash

# Pythonスクリプトを使用してDocker Composeの起動をチェック
python3 /my/location/check_step6.py

# Pythonスクリプトの終了コードをスクリプトの終了コードとして設定
exit $?
