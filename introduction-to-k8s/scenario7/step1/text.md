(※ スクリプトの実行が完了してから開始してください)  
イメージ `redis:alpine` を使用して、ネットワーク `lab-network` に接続された `redis` という名前のコンテナを detached モードで起動してください。  
(`lab-network` はすでに作成されています)

- コンテナ名：`redis`
- イメージ：`redis:alpine`
- ネットワーク：`lab-network`


<details>
  <summary>Solution</summary>

`docker container run -d --name redis --network lab-network redis:alpine`{{execute}} コマンドを実行します。

</details>