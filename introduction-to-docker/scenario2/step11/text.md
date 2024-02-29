以下の条件でコンテナをバックグラウンド (detached モード) で起動してください。

- コンテナ名：mysql-db
- イメージ：mysql
- 環境変数：MYSQL_ROOT_PASSWORD=db_pass123

<details>
  <summary>Hints</summary>

`-e MYSQL_ROOT_PASSWORD=db_pass123` で環境変数を設定します。

</details>

<details>
  <summary>Solution</summary>

`docker run -d -e MYSQL_ROOT_PASSWORD=db_pass123 --name mysql-db mysql`{{execute}} を実行します。
コンテナ内から環境変数を確認するには `docker exec -it mysql-db env`{{execute}}を実行します。 

</details>