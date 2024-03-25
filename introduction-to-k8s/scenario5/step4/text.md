Deployment `frontend` の現在の `StrategyType` は何ですか。

- [ ] Recreate
- [ ] BlueGreen
- [ ] RollingUpdate
- [ ] Canary

<details>
  <summary>Hints</summary>

`kubectl describe deployment` コマンドを使用して `StrategyType` を確認します。

</details>

<details>
  <summary>Solution</summary>

`kubectl describe deployment frontend | grep -i strategy`{{execute}} コマンドを実行します。

</details>

<details>
  <summary>Answer</summary>

RollingUpdate

</details>