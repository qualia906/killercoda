命令型コマンドを使用して、以下の設定で Deployment を作成してください。

- Deployment 名：`webapp`
- イメージ：`qualia906/simple-webapp`
- レプリカ数：`3`

<details>
  <summary>Hints</summary>

`kubectl create deployment` コマンドを使用します。

</details>

<details>
  <summary>Solution</summary>

`kubectl create deployment webapp --image=qualia906/simple-webapp --replicas=3`{{execute}} を実行します。

</details>