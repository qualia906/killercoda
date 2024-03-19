import sys

# シェルスクリプトからの出力を取得
output = sys.argv[1]

# 出力を行ごとに分割
lines = output.split('\n')

# 指定された条件を満たしているかチェック
command_executed = False
for line in lines:
    if not line.strip():
        # 空行は無視
        continue
    name, image = line.split()
    if name == 'redis' and image == 'redis123':  # 名前が厳密に 'redis' と一致するかチェック
        command_executed = True
        break

# 結果に基づいて終了コードを返す
if command_executed:
    sys.exit(0)
else:
    sys.exit(1)
