(※ スクリプトの実行が完了してから開始してください)  
`lab-pod` という名前の Pod を作成しました。  
この Pod で使用されているコンテナイメージは以下のどれですか。

- [ ] nginx
- [ ] ubutu
- [ ] redis
- [ ] webapp

> 設問の中でスクリプトが実行されることがあります。  
> この場合は、スクリプトの実行が完了し **Done** が出力されてから作業を開始してください。

<details>
  <summary>Hints</summary>

`kubectl describe pod` コマンドを使用します。

</details>

<details>
  <summary>Solution</summary>

`kubectl describe pod lab-pod | grep Image`{{execute}} コマンドを実行し、`Image` セクションの値を確認します。

</details>

<details>
  <summary>Answer</summary>

redis

</details>
