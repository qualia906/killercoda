StatefulSet `nginx` の Pod である `nginx-2` を削除してください。  
削除を実行した後の StatefulSet `nginx` Pod はどれですか。

- [ ] nginx-1, nginx-3
- [ ] nginx-0, nginx-1
- [ ] nginx-0, nginx-1, nginx-2
- [ ] nginx-0, nginx-1, nginx-3


<details>
  <summary>Solution</summary>

`kubectl delete pod nginx-2`{{execute}} を実行して Pod `nginx-2` を削除します。  
`kubectl get pods`{{execute}} を実行して StatefulSet `nginx` の現在の Pod を確認します。

</details>

<details>
  <summary>Answer</summary>

nginx-0, nginx-1, nginx-2

> レプリカ数を維持するように StatefulSet によって Pod `nginx-2` が再作成されました。  

</details>
