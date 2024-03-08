新しく作成された Pod には何のイメージが使用されていますか。

- [ ] nginx
- [ ] busybox
- [ ] jenkins
- [ ] newpods

<details>
  <summary>Hints</summary>

`kubectl describe` コマンドを使用します。

</details>

<details>
  <summary>Solution</summary>

`kubectl describe pod newpods-<id>`{{copy}} コマンドを実行し、`containers` セクションを確認します。

</details>