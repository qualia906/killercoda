Pod `webapp` には何のイメージが使用されていますか？

- [ ] nginx & redis
- [ ] appsrvx
- [ ] nginx & appsrvx
- [ ] busybox
- [ ] nginx


<details>
  <summary>Hints</summary>

`kubectl describe` コマンドを使用します。

</details>

<details>
  <summary>Solution</summary>

`kubectl describe pod webapp`{{execute}} を実行し、各コンテナで使用されているイメージを確認します。

</details>

<details>
  <summary>Answer</summary>

nginx & appsrvx

</details>
