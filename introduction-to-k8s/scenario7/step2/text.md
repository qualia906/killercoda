以下の設定で、ネットワーク `lab-network` に接続された `clickcounter` という名前のコンテナを detached モードで起動してください。

- コンテナ名：`clickcounter`
- イメージ：`qualia906/click-counter`
- コンテナポート：`5000`
- ホストポート：`8085`
- ネットワーク：`lab-network`


<details>
  <summary>Solution</summary>

`docker container run -d --name clickcounter -p 8085:5000 --network lab-network qualia906/click-counter`{{execute}} コマンドを実行します。

</details>
