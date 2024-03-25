Deployment `frontend` では、Rolling Update の際、一度に何個までの Pod が削除されますか。

- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4


<details>
  <summary>Hints</summary>

`kubectl describe deployment frontend` を実行し、`maxUnavailable` フィールドを確認します。  
https://kubernetes.io/ja/docs/concepts/workloads/controllers/deployment/#deployment%E3%81%AE%E3%83%AD%E3%83%BC%E3%83%AA%E3%83%B3%E3%82%B0%E3%82%A2%E3%83%83%E3%83%97%E3%83%87%E3%83%BC%E3%83%88

</details>


<details>
  <summary>Solution</summary>

`kubectl describe deployment frontend` を実行すると、`maxUnavailable` フィールドが `25%` であることがわかります。これは、Rolling Update の際、一度にレプリカ数 4 個のうちの 25%　まで、すなわち 1 個の Pod が削除されることを意味します。

```
  strategy:
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 25%
    type: RollingUpdate
```

</details>

<details>
  <summary>Answer</summary>

1

</details>
