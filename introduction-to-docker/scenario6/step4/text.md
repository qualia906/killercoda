イメージ `alpine` を使用して、ネットワーク `none` に接続された `alpine-2` という名前のコンテナを実行してください。  
(コンテナは起動直後に停止しても構いません) 

<details>
  <summary>Hints</summary>

ネットワークへの接続を設定するには `docker container run` コマンドで `--network=none` を指定します。

</details>

<details>
  <summary>Solution</summary>

`docker container run --name alpine-2 --network=none alpine`{{execute}} コマンドを実行します。

</details>