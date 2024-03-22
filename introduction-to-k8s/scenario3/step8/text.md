Deployment `frontend-dep` の Pod では何のイメージが使用されていますか。

- [ ] nginx
- [ ] frontend
- [ ] busybox
- [ ] busybox999


<details>
  <summary>Hints</summary>

`kubectl describe` コマンドを使用して Deployment あるいは Pod のイメージを確認します。

</details>

<details>
  <summary>Solution</summary>

`kubectl describe deployment frontend-dep | grep Image`{{execute}} を実行します。  
または、`kubectl describe pod <POD_NAME>`{{copy}} を実行して `Image` フィールドを確認します。

</details>

<details>
  <summary>Answer</summary>

busybox999

</details>