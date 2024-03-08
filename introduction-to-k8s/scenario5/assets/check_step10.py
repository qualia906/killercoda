import sys
import subprocess
import json

def check_container_details(container_name):
    # Dockerコンテナの詳細情報を取得
    result = subprocess.run(['docker', 'inspect', container_name], capture_output=True, text=True)
    details = json.loads(result.stdout)

    # コンテナがnginx:latestイメージから作成されていることをチェック
    if 'nginx:latest' not in details[0]['Config']['Image']:
        print(f"Container {container_name} is not created from nginx:latest image.")
        return False

    # コンテナがdetachedモードで実行されていることをチェック
    if details[0]['Config']['AttachStdout'] or details[0]['Config']['AttachStderr']:
        print(f"Container {container_name} is not running in detached mode.")
        return False

    # ボリュームが適切にマウントされていることをチェック
    if '/usr/local/share/my-volume' not in details[0]['Mounts'][0]['Destination']:
        print(f"Volume my-volume is not mounted to /usr/local/share/my-volume in container {container_name}.")
        return False

    return True

if __name__ == '__main__':
    container_name = sys.argv[1]
    if check_container_details(container_name):
        print(f"Container {container_name} is created correctly.")
        sys.exit(0)
    else:
        sys.exit(1)
