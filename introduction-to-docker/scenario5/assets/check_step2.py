import sys
import subprocess
import json

def check_container_config(container_name):
    # Dockerコンテナの詳細情報を取得
    result = subprocess.run(['docker', 'inspect', container_name], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Failed to inspect container {container_name}")
        return False

    details = json.loads(result.stdout)

    # イメージがalpineであることをチェック
    if 'alpine' not in details[0]['Config']['Image']:
        print(f"Container {container_name} is not using alpine image.")
        return False

    # コマンドが`sleep 1000`であることをチェック
    if details[0]['Config']['Cmd'] != ['sleep', '1000']:
        print(f"Container {container_name} does not execute sleep 1000.")
        return False

    # Detachedモードで実行されているかをチェック
    if details[0]['Config']['AttachStdout'] or details[0]['Config']['AttachStderr']:
        print(f"Container {container_name} is not running in detached mode.")
        return False

    print(f"Container {container_name} is configured correctly.")
    return True

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python check_container_config.py <container_name>")
        sys.exit(1)

    container_name = sys.argv[1]
    if check_container_config(container_name):
        sys.exit(0)
    else:
        sys.exit(1)
