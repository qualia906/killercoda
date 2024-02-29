以下の条件でコンテナをバックグラウンド (detached モード) で起動してください。

- コンテナ名：`green-app`
- イメージ：`kodekloud/simple-webapp`
- 環境変数：`APP_COLOR=green`
- コンテナポート：`8080`
- ホストポート：`38285`

<details>
  <summary>Hints</summary>

`-p 38285:8080` でポートマッピングを設定します。  
`-e APP_COLOR=green` で環境変数を設定します。

</details>

<details>
  <summary>Solution</summary>

`docker container run -d -p 38285:8080 -e APP_COLOR=green --name green-app kodekloud/simple-webapp`{{execute}} を実行します。 

</details>
