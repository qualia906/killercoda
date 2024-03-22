import sys

# シェルスクリプトからの出力を取得
deployment_output = sys.argv[1]
pods_output = sys.argv[2]

# Deployment の条件を確認
name, image, replicas = deployment_output.split()
if not (name == 'httpd-frontend' and image == 'httpd:2.4-alpine' and int(replicas) == 3):
    sys.exit(1)  # 条件を満たさない場合は終了コード1で終了

# Pod の状態を確認
running_pods = 0
for line in pods_output.split('\n'):
    if not line.strip():
        continue  # 空行は無視
    _, status = line.split()
    if status == 'Running':
        running_pods += 1

# 関連するPodが全てRunning状態であることを確認
if running_pods == int(replicas):
    sys.exit(0)  # 条件を満たす場合は終了コード0で終了
else:
    sys.exit(1)  # 条件を満たさない場合は終了コード1で終了