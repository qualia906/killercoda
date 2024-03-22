この環境に Serivice はいくつ存在しますか。  
(Namespace `default` について)

- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3

<details>
  <summary>Hints</summary>

`kubectl get services` コマンドを使用します。  
短縮名を使用して `kubectl get svc` と書くこともできます。

</details>

<details>
  <summary>Solution</summary>

`kubectl get svc`{{execute}} を実行します。  

</details>

<details>
  <summary>Answer</summary>

1
> これは Kubernetes によって予め作成されているデフォルトの Service です。

</details>
