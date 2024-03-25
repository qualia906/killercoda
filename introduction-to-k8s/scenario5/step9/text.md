Deployment `frontend` のアプリケーションのバージョンを Version 1 にロールバックしてください。
以下のリンクからアプリケーションにアクセスして、ロールバックされたことを確認してください。
{{TRAFFIC_HOST1_30080}}

<details>
  <summary>Hints</summary>

`kubectl rollout undo` コマンドを使用します。  
または `/root/manifests/frontend-deployment.yaml` を編集して `image` フィールドを元の値に戻すこともできます。  

</details>

<details>
  <summary>Solution</summary>

`kubectl rollout undo deployment frontend`{{execute}} を実行します。

</details>