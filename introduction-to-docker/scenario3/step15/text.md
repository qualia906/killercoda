`ubuntu` イメージを使用して、起動時に `sleep 1000` を実行するようにコンテナを起動してください。detached モードで起動してください。  
(`Dockerfile-ubuntu` からイメージを自身でビルドする必要はありません)


<details>
  <summary>Hints</summary>

`ubuntu` イメージでは `CMD` でデフォルトのコマンドだけが指定されているため、`docker container run` コマンドで `sleep 1000` を指定することで起動時コマンドをオーバーライドできます。

</details>

<details>
  <summary>Solution</summary>

`docker container run -d ubuntu sleep 1000`{{exec}} を実行します。

</details>