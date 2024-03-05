以下の設定でネットワーク `mysql-network` に接続された mysql コンテナを detached モードで作成してください。
データベースのパスワードも環境変数で設定します。

- コンテナ名：`mysql-db`
- イメージ：`mysql:5.6`
- 環境変数：`MYSQL_ROOT_PASSWORD=db_pass123`
- ネットワーク：`mysql-network`

<details>
  <summary>Hints</summary>

- 接続するネットワークを設定するには、`docker container run` コマンドで `--network` フラグを指定します。
- 環境変数を設定するには、`-e` フラグを指定します。

</details>

<details>
  <summary>Solution</summary>

`docker container run -d --name mysql-db -e MYSQL_ROOT_PASSWORD=db_pass123 --network mysql-network mysql:5.6`{{execute}} を実行します。

</details>
