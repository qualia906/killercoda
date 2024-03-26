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

    conditions_met = (
        deployment_name == 'test-2' and
        replicas == 2 and
        match_labels == {'app': 'test-2'} and
        container_image == 'nginx'
    )

    if conditions_met:
        sys.exit(0)  # 条件を満たす
    else:
        sys.exit(1)  # 条件を満たさない
except KeyError:
    sys.exit(1)  # 必要なキーが存在しない場合
