import sys
import json

# シェルスクリプトからの出力（JSON形式）を取得してPythonの辞書に変換
output_json = json.loads(sys.argv[1])

# 条件を満たしているかチェック
try:
    service_name = output_json['metadata']['name']
    namespace = output_json['metadata']['namespace']
    ports = output_json['spec']['ports'][0]
    selector = output_json['spec']['selector']
    type = output_json['spec']['type']

    conditions_met = (
        service_name == 'frontend-service' and
        namespace == 'default' and
        ports['port'] == 8080 and
        ports['nodePort'] == 30080 and
        ports['targetPort'] == 8080 and
        selector == {'name': 'webapp', 'version': 'v2'} and
        type == 'NodePort'
    )

    if conditions_met:
        sys.exit(0)  # 条件を満たす
    else:
        sys.exit(1)  # 条件を満たさない
except KeyError:
    sys.exit(1)  # 必要なキーが存在しない場合
