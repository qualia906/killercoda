import sys
import json

# シェルスクリプトからの出力（JSON形式）を取得してPythonの辞書に変換
output_json = json.loads(sys.argv[1])

# 条件を満たしているかチェック
try:
    pod_name = output_json['metadata']['name']
    container = output_json['spec']['containers'][0]
    container_name = container['name']
    container_image = container['image']
    volume_mounts = container['volumeMounts'][0]
    volumes = output_json['spec']['volumes'][0]
    pvc_claim_name = volumes['persistentVolumeClaim']['claimName']

    if (pod_name == 'pod-pv' and
        container_image == 'nginx' and volume_mounts['mountPath'] == "/var/www/html" and
        pvc_claim_name == 'pvc-1'):
        sys.exit(0)  # 条件を満たす
    else:
        sys.exit(1)  # 条件を満たさない
except KeyError:
    sys.exit(1)  # 必要なキーが存在しない場合
