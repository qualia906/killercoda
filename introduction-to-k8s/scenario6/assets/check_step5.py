import sys
import json

# シェルスクリプトからの出力（JSON形式）を取得してPythonの辞書に変換
output_json = json.loads(sys.argv[1])

# 条件を満たしているかチェック
try:
    pvc_name = output_json['metadata']['name']
    storage_class_name = output_json['spec']['storageClassName']
    access_modes = output_json['spec']['accessModes']
    storage_request = output_json['spec']['resources']['requests']['storage']

    if (pvc_name == 'pvc-1' and storage_class_name == 'local-path' and 
        'ReadWriteOnce' in access_modes and storage_request == '1Gi'):
        sys.exit(0)  # 条件を満たす
    else:
        sys.exit(1)  # 条件を満たさない
except KeyError:
    sys.exit(1)  # 必要なキーが存在しない場合
