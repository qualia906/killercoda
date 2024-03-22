作成された Deployment `frontend-dep` のレプリカ数はいくつですか。

- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4

<details>
  <summary>Hints</summary>

`kubectl get deployments` あるいは `kubectl describe deployment` コマンドを使用して確認できます。
また、`kubectl get pods` コマンドを使用して実際の Pod 数を確認することもできます。
 
</details>

<details>
  <summary>Solution</summary>

`kubectl describe deployment frontend-dep | grep Replicas`{{execute}} を実行します。 
 
</details>

<details>
  <summary>Answer</summary>

4

</details>