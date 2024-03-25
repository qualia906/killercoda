import sys
import json

# シェルスクリプトからの出力（JSON形式）を取得してPythonの辞書に変換
output_json = json.loads(sys.argv[1])

# 条件を満たしているかチェック
try:
    deployment_name = output_json['metadata']['name']
    replicas = output_json['spec']['replicas']
    match_labels = output_json['spec']['selector']['matchLabels']
    container_image = output_json['spec']['template']['spec']['containers'][0]['image']
    container_name = output_json['spec']['template']['spec']['containers'][0]['name']
    container_port = output_json['spec']['template']['spec']['containers'][0]['ports'][0]['containerPort']

    if (deployment_name == 'frontend-canary' and replicas == 1 and 
        match_labels == {'name': 'webapp', 'version': 'v3'} and
        container_image == 'qualia906/webapp-color:v3' and
        container_port == 8080):
        sys.exit(0)  # 条件を満たす
    else:
        sys.exit(1)  # 条件を満たさない
except KeyError:
    sys.exit(1)  # 必要なキーが存在しない場合
