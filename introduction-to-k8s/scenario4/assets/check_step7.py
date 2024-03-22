import sys
import json

# シェルスクリプトからの出力（JSON形式）を取得してPythonの辞書に変換
output_json = json.loads(sys.argv[1])

# 条件を満たしているかチェック
try:
    service_name = output_json["metadata"]["name"]
    namespace = output_json["metadata"]["namespace"]
    port = output_json["spec"]["ports"][0]["port"]
    target_port = output_json["spec"]["ports"][0]["targetPort"]
    node_port = output_json["spec"]["ports"][0]["nodePort"]
    selector_app = output_json["spec"]["selector"]["app"]
    type = output_json["spec"]["type"]

    if (service_name == "webapp-service" and namespace == "default" and
            port == 8080 and target_port == 8080 and node_port == 30080 and
            selector_app == "webapp" and type == "NodePort"):
        sys.exit(0)  # 条件を満たす
    else:
        sys.exit(1)  # 条件を満たさない
except KeyError:
    sys.exit(1)  # 必要なキーが存在しない場合
