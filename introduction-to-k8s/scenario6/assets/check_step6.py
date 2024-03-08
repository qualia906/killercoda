import sys
import subprocess
import json

def check_container_config(container_name):
    # Dockerコンテナの詳細情報を取得
    result = subprocess.run(['docker', 'inspect', container_name], capture_output=True, text=True)
    details = json.loads(result.stdout)

    # コンテナがmysql:5.6イメージから作成されていることをチェック
    if 'mysql:5.6' not in details[0]['Config']['Image']:
        print(f"Container {container_name} is not created from mysql:5.6 image.")
        return False

    # 環境変数MYSQL_ROOT_PASSWORDがdb_pass123に設定されていることをチェック
    env_vars = details[0]['Config']['Env']
    if "MYSQL_ROOT_PASSWORD=db_pass123" not in env_vars:
        print("Environment variable MYSQL_ROOT_PASSWORD is not set to db_pass123.")
        return False

    # コンテナがmysql-networkネットワークに接続されていることをチェック
    network_settings = details[0]['NetworkSettings']['Networks']
    if 'mysql-network' not in network_settings:
        print("Container is not connected to network mysql-network.")
        return False

    # コンテナがdetachedモードで実行されていることをチェック
    if details[0]['Config']['AttachStdout'] or details[0]['Config']['AttachStderr']:
        print(f"Container {container_name} is not running in detached mode.")
        return False

    return True

if __name__ == '__main__':
    container_name = sys.argv[1]
    if check_container_config(container_name):
        print(f"Container {container_name} is configured correctly.")
        sys.exit(0)
    else:
        sys.exit(1)
