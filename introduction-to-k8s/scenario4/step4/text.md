Service `kubernetes` にはいくつの `label` が設定されていますか。

- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3


<details>
  <summary>Hints</summary>

`kubectl describe svc` コマンドを使用します。  

</details>

<details>
  <summary>Solution</summary>

`kubectl describe svc kubernetes`{{execute}} を実行し、`Labels` フィールドを確認します。  

</details>

<details>
  <summary>Answer</summary>

2

</details>