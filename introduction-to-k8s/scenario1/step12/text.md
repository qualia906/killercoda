以下の設定で Pod を作成してください。

- Pod 名：`redis`
- イメージ：`redis:alpine`

<details>
  <summary>Hints</summary>

`kubectl run` コマンドを使用します。  

</details>

<details>
  <summary>Solution</summary>

`kubectl run redis --image redis:alpine`{{execute}} コマンドを実行します。

</details>