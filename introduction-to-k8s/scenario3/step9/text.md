ビルドしたイメージ `color-webapp` を使用して、以下の設定でコンテナを起動してください。

- イメージ：`color-webapp`
- コンテナポート：`8080`
- ホストポート：`8282`

<details>
  <summary>Hints</summary>

`-p 8282:8080` でポートマッピングを設定します。  

</details>

<details>
  <summary>Solution</summary>

`docker container run -d -p 8282:8080 color-webapp`{{execute}} を実行します。 

</details>
