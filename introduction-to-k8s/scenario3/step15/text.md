Namespace `finance` に以下の設定で Pod を 1 つ作成してください。  

- Pod 名: `pod-1`
- イメージ: `redis`


<details>
  <summary>Hints</summary>

`kubectl run` コマンドで `-n` フラグを指定します。

</details>

<details>
  <summary>Solution</summary>

`kubectl run pod-1 -n finance --image redis`{{execute}} を実行します。

</details>