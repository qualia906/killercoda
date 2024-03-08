実行したコンテナに設定されている環境変数 `APP_COLOR` の値は以下のどれですか。

- [ ] red
- [ ] blue
- [ ] green
- [ ] pink

<details>
  <summary>Hints</summary>

まず `docker container ls` コマンドを実行し、コンテナ ID かコンテナ名を確認します。  
そして `docker container inspect <CONTAINER_ID | CONTAINER_NAME>`{{copy}} コマンドを実行し `Env` セクションを確認します。

</details>

<details>
  <summary>Solution</summary>

`docker container inspect <CONTAINER_ID | CONTAINER_NAME> | grep -A 10 Env`{{copy}} を実行します。

</details>

<details>
  <summary>Answer</summary>

blue

</details>
