import sys
import json

# シェルスクリプトからの出力（JSON形式）を取得してPythonの辞書に変換
output_json = json.loads(sys.argv[1])

# 条件を満たしているかチェック
try:
    name = output_json['metadata']['name']
    replicas = output_json['spec']['replicas']
    container_image = output_json['spec']['template']['spec']['containers'][0]['image']
    container_port = output_json['spec']['template']['spec']['containers'][0]['ports'][0]['containerPort']
    mount_path = output_json['spec']['template']['spec']['containers'][0]['volumeMounts'][0]['mountPath']
    pvc_access_modes = output_json['spec']['volumeClaimTemplates'][0]['spec']['accessModes'][0]
    pvc_storage_class_name = output_json['spec']['volumeClaimTemplates'][0]['spec']['storageClassName']
    pvc_resources_requests_storage = output_json['spec']['volumeClaimTemplates'][0]['spec']['resources']['requests']['storage']

    conditions_met = (
        name == 'nginx' and
        replicas == 3 and
        container_image == 'nginx:latest' and
        container_port == 8080 and
        mount_path == '/data' and  # mountPath のチェックを追加
        pvc_access_modes == 'ReadWriteOnce' and
        pvc_storage_class_name == 'local-path' and
        pvc_resources_requests_storage == '50Mi'
    )

    if conditions_met:
        sys.exit(0)  # 条件を満たす
    else:
        sys.exit(1)  # 条件を満たさない
except KeyError:
    sys.exit(1)  # 必要なキーが存在しない場合
