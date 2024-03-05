import sys
import subprocess
import json

def check_container_config(container_name):
    # Dockerコンテナの詳細情報を取得
    result = subprocess.run(['docker', 'inspect', container_name], capture_output=True, text=True)
    details = json.loads(result.stdout)

    # コンテナがqualia906/simple-webapp-mysqlイメージから作成されていることをチェック
    if 'qualia906/simple-webapp-mysql' not in details[0]['Config']['Image']:
        print(f"Container {container_name} is not created from qualia906/simple-webapp-mysql image.")
        return False

    # Detachedモードで実行されていることをチェック
    if details[0]['Config']['AttachStdout'] or details[0]['Config']['AttachStderr']:
        print(f"Container {container_name} is not running in Detached mode.")
        return False

    # ネットワーク設定をチェック
    if 'mysql-network' not in details[0]['NetworkSettings']['Networks']:
        print(f"Container {container_name} is not connected to mysql-network.")
        return False

    # 環境変数をチェック
    env_vars = details[0]['Config']['Env']
    if "DB_Host=mysql-db" not in env_vars or "DB_Password=db_pass123" not in env_vars:
        print("Environment variables are not set correctly.")
        return False

    # ポートマッピングをチェック
    port_bindings = details[0]['HostConfig']['PortBindings']
    if '8080/tcp' not in port_bindings or port_bindings['8080/tcp'][0]['HostPort'] != '38080':
        print("Port mapping is not set correctly.")
        return False

    return True

if __name__ == '__main__':
    container_name = sys.argv[1]
    if check_container_config(container_name):
        print(f"Container {container_name} is configured correctly.")
        sys.exit(0)
    else:
        sys.exit(1)
