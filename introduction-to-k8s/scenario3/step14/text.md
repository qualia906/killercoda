namespace `research` には何個の Pod が存在しますか。

- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3


<details>
  <summary>Hints</summary>

`kubectl get pods` コマンドで `-n` フラグを指定します。

</details>

<details>
  <summary>Solution</summary>

`kubectl get pods -n research`{{execute}} を実行します。

</details>

<details>
  <summary>Answer</summary>

2

</details>