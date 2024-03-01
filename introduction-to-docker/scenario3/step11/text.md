ベースイメージであるイメージ `python:3.6` で使用されている OS は以下のどれですか。  
必要があれば新たにコンテナを起動しても構いません。

- [ ] centos
- [ ] debian
- [ ] rhel
- [ ]ubuntu


<details>
  <summary>Hints</summary>

コンテナ内で `cat /etc/*release*` を実行することで OS を確認できます。
`color-webapp` のコンテナがすでに停止している場合は、イメージ `python:3.6` から新たにコンテナを起動して確認します。  
`color-webapp` のコンテナが起動している場合は、`docker container exec` コマンドを使用してコンテナ内で `cat /etc/*release*` を実行することもできます。

</details>

<details>
  <summary>Solution</summary>

以下のどちらかを実行します。

- `docker container run python:3.6 cat /etc/*release*`{{exec}}
- `docker container exec <CONTAINER_ID | CONTAINER_NAME> cat /etc/*release*`{{copy}}

</details>

<details>
  <summary>Answer</summary>

debian

</details>
