以下の設定で、ネットワーク `mysql-network` に接続された `webapp` という名前のコンテナを実行してください。

- コンテナ名：`webapp`
- イメージ：`kodekloud/simple-webapp-mysql`
- 環境変数：`DB_Host=mysql-db`
- コンテナポート：`8080`
- ホストポート：`38080`
- ネットワーク：`mysql-network`


<details>
  <summary>Hints</summary>

- 接続するネットワークを設定するには、`docker container run` コマンドで `--network` フラグを指定します。
- 環境変数を設定するには、`-e` フラグを指定します。

</details>


<details>
  <summary>Solution</summary>

`docker container run -d --name webapp --network mysql-network -e DB_Host=mysql-db -p 38080:8080 kodekloud/simple-webapp-mysql`{{execute}} を実行します。

</details>