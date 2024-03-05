import sys
import subprocess
import json

def check_container_config(container_name):
    # Dockerコンテナの詳細情報を取得
    result = subprocess.run(['docker', 'inspect', container_name], capture_output=True, text=True)
    details = json.loads(result.stdout)

    # コンテナがalpineイメージから作成されていることをチェック
    if 'alpine' not in details[0]['Config']['Image']:
        print(f"Container {container_name} was not created from alpine image.")
        return False

    # コンテナのネットワークモードがnoneであることをチェック
    if details[0]['HostConfig']['NetworkMode'] != 'none':
        print(f"Container {container_name} has network mode other than none.")
        return False

    return True

if __name__ == '__main__':
    container_name = sys.argv[1]
    if check_container_config(container_name):
        print(f"Container {container_name} is configured correctly.")
        sys.exit(0)
    else:
        sys.exit(1)
