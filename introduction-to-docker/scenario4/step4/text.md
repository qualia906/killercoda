このホストにプライベート レジストリを作成してください。

- コンテナ名：`my-registry`
- ホストポート：`5000`


<details>
  <summary>Hints</summary>

プライベート レジストリを作成するには以下の設定で detached モードでコンテナを実行します。

- イメージ：`registry:2`
- コンテナポート：`5000`

また、実際の使用時には、可用性の観点から `docker container run` コマンドで `--restart=always` フラグを設定します。 

</details>

<details>
  <summary>Solution</summary>

`docker container run -d -p 5000:5000 --name my-registry registry:2`{{execute}} を実行します。

</details>