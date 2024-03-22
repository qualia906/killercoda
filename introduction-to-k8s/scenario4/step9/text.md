Deployment `backend-redis` を新たに作成しました。  
クラスタ内のアプリケーションからアクセスできるように、以下の設定で Service を構成して `backend-redis` を公開してください。  
(※ マニフェスト ファイルは使用せず、命令型コマンドで実行してください)

- Service 名： `redis-service`
- type： `ClusterIP`
- port： `6379`


<details>
  <summary>Hints</summary>

`kubectl expose deployment` コマンドを使用して、Deployment を公開できます。

</details>

<details>
  <summary>Solution</summary>

`kubectl expose deployment backend-redis --type=ClusterIP --port=6379 --name=redis-service`{{execute}} コマンドを実行します。

</details>

