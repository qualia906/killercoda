import sys
import json

# シェルスクリプトからの出力（JSON形式）を取得してPythonの辞書に変換
output_json = json.loads(sys.argv[1])

# 条件を満たしているかチェック
try:
    service_name = output_json["metadata"]["name"]
    type = output_json["spec"]["type"]
    port = output_json["spec"]["ports"][0]["port"]

    if service_name == "redis-service" and type == "ClusterIP" and port == 6379:
        sys.exit(0)  # 条件を満たす
    else:
        sys.exit(1)  # 条件を満たさない
except KeyError:
    sys.exit(1)  # 必要なキーが存在しない場合
