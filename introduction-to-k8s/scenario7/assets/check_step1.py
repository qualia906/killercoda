import sys
import subprocess
import json

def check_container_config(container_name):
    # Dockerコンテナの詳細情報を取得
    result = subprocess.run(['docker', 'inspect', container_name], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Failed to get info of container {container_name}.")
        return False

    details = json.loads(result.stdout)

    # コンテナがredis:alpineイメージから作成されていることをチェック
    if 'redis:alpine' not in details[0]['Config']['Image']:
        print(f"Container {container_name} is not created from redis:alpine image.")
        return False

    # コンテナがdetachedモードで実行されていることをチェック
    if details[0]['Config']['AttachStdout'] or details[0]['Config']['AttachStderr']:
        print(f"Container {container_name} is not running in detached mode.")
        return False

    # コンテナが指定されたネットワークに接続されていることをチェック
    if 'lab-network' not in details[0]['NetworkSettings']['Networks']:
        print(f"Container {container_name} is not connected to lab-network.")
        return False

    return True

if __name__ == '__main__':
    container_name = sys.argv[1]
    if check_container_config(container_name):
        print(f"Container {container_name} is configured correctly.")
        sys.exit(0)
    else:
        sys.exit(1)
