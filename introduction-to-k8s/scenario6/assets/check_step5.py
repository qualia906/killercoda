import sys
import subprocess
import json

def check_network_config(network_name):
    # Dockerネットワークの詳細情報を取得
    result = subprocess.run(['docker', 'network', 'inspect', network_name], capture_output=True, text=True)
    details = json.loads(result.stdout)

    # ネットワークのドライバーがbridgeであることをチェック
    if details[0]['Driver'] != 'bridge':
        print(f"Network {network_name} has wrong driver.")
        return False

    # サブネットとゲートウェイをチェック
    config = details[0]['IPAM']['Config'][0]
    if config['Subnet'] != '182.18.0.1/24' or config['Gateway'] != '182.18.0.1':
        print(f"Network {network_name} has wrong subnet or gateway.")
        return False

    return True

if __name__ == '__main__':
    network_name = sys.argv[1]
    if check_network_config(network_name):
        print(f"Network {network_name} is configured correctly.")
        sys.exit(0)
    else:
        sys.exit(1)
