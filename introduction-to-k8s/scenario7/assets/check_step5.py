import sys
import yaml

def check_compose_content(file_path):
    # docker-compose.yml ファイルを読み込む
    with open(file_path, 'r') as file:
        compose_data = yaml.safe_load(file)
    
    # 特定のサービスと設定が存在するかチェック
    services = compose_data.get('services', {})
    if not all(key in services for key in ['redis', 'clickcounter']):
        print("必要なサービスが docker-compose.yml に含まれていません。")
        return False

    # redis サービスのイメージが正しいかチェック
    if services['redis'].get('image') != 'redis:alpine':
        print("redis サービスのイメージが正しくありません。")
        return False

    # clickcounter サービスの設定をチェック
    clickcounter = services['clickcounter']
    if clickcounter.get('image') != 'qualia906/click-counter' or '8085:5000' not in clickcounter.get('ports', []):
        print("clickcounter サービスの設定が正しくありません。")
        return False

    # バージョンが正しいかチェック
    if compose_data.get('version') != '3.7':
        print("docker-compose ファイルのバージョンが正しくありません。")
        return False

    return True

if __name__ == '__main__':
    if check_compose_content(sys.argv[1]):
        print("docker-compose.yml ファイルはすべてのチェックを通過しました。")
        sys.exit(0)
    else:
        sys.exit(1)
