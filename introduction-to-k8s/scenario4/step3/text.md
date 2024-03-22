Service `kubernetes` に設定されている `TargetPort` はどれですか。

- [ ] 80
- [ ] 443
- [ ] 6443
- [ ] 8080


<details>
  <summary>Hints</summary>

`kubectl describe svc` コマンドを使用します。  

</details>

<details>
  <summary>Solution</summary>

`kubectl describe svc kubernetes | grep TargetPort`{{execute}} を実行します。  

</details>

<details>
  <summary>Answer</summary>

6443

</details>
