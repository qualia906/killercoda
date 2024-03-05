import subprocess
import json
import sys

def check_container_config():
    # 実行中のコンテナの詳細情報を取得
    result = subprocess.run(['docker', 'ps', '-a', '--format', '{{.Names}}'], capture_output=True, text=True)
    if result.returncode != 0:
        print("コンテナのリスト取得に失敗しました。")
        return False

    container_names = result.stdout.split()

    # 期待する設定
    expected_configs = {
        "redis": {
            "image": "redis:alpine",
        },
        "clickcounter": {
            "image": "qualia906/click-counter",
            "ports": ["8085:5000"],
        }
    }

    # コンテナごとに設定を検証
    for name, config in expected_configs.items():
        if name not in container_names:
            print(f"コンテナ {name} は実行中ではありません。")
            return False
        
        # コンテナの詳細情報を取得
        inspect_result = subprocess.run(['docker', 'inspect', name], capture_output=True, text=True)
        details = json.loads(inspect_result.stdout)

        # イメージを検証
        if config["image"] not in details[0]["Config"]["Image"]:
            print(f"コンテナ {name} はイメージ {config['image']} から作成されていません。")
            return False

        # ポートを検証（clickcounterのみ）
        if "ports" in config:
            ports = details[0]["HostConfig"]["PortBindings"]
            for port in config["ports"]:
                internal, external = port.split(":")
                if f"{internal}/tcp" not in ports or ports[f"{internal}/tcp"][0]["HostPort"] != external:
                    print(f"コンテナ {name} のポート {port} が正しくマッピングされていません。")
                    return False

    return True

if __name__ == "__main__":
    if check_container_config():
        print("すべてのコンテナは指定された設定で正しく実行されています。")
        sys.exit(0)
    else:
        sys.exit(1)
