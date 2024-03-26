import sys
import json

# シェルスクリプトからの出力（JSON形式）を取得してPythonの辞書に変換
output_json = json.loads(sys.argv[1])

# 条件を満たしているかチェック
try:
    pod_name = output_json['metadata']['name']
    container_image = output_json['spec']['containers'][0]['image']

    if pod_name == 'test-1' and container_image == 'nginx:latest':
        sys.exit(0)  # 条件を満たす
    else:
        sys.exit(1)  # 条件を満たさない
except KeyError:
    sys.exit(1)  # 必要なキーが存在しない場合
