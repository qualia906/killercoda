これらの Pod はどのノードにデプロイされていますか。  
Pod の詳細を確認して回答してください。

- [ ] master
- [ ] master & node01
- [ ] controlplane
- [ ] node01
- [ ] node02


<details>
  <summary>Hints</summary>

`-o wide` オプションを使用して `kubectl get` コマンドを実行します。

</details>

<details>
  <summary>Solution</summary>

`kubectl get pods -o wide`{{execute}} を実行して `NODE` 列を確認します。

</details>

<details>
  <summary>Answer</summary>

controlplane

</details>

