namespace `dev` に以下の設定で `deploy-3` という名前の Deployment を作成してください。  

- Deployment 名： `deploy-3`  
- イメージ： `redis`  
- replicas: `3`  


<details>
  <summary>Hints</summary>

`kubectl create deployment` コマンドで `-n` フラグを指定します。

</details>

<details>
  <summary>Solution</summary>

`kubectl create deployment deploy-3 -n dev --image redis --replicas 3`{{execute}} を実行します。

</details>