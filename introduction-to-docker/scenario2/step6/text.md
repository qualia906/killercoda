以下の条件でコンテナをバックグラウンド (detached モード) で起動してください。

- イメージ：`qualia906/simple-webapp`
- タグ：`bule`
- コンテナポート：`8080`
- ホストポート：`38282`

<details>
  <summary>Hints</summary>

`-p 38282:8080` でポートマッピングを設定します。

</details>

<details>
  <summary>Solution</summary>

`docker container run -d -p 38282:8080 qualia906/simple-webapp:blue`{{execute}} を実行します。 

</details>