StatefulSet `nginx` に管理されている Pod は以下のどれですか。

- [ ] nginx-1, nginx-2, nginx-3
- [ ] nginx-0, nginx-1, nginx-2
- [ ] nginx-a, nginx-b, nginx-c
- [ ] nginx-<ランダムな文字列>


<details>
  <summary>Solution</summary>

`kubectl get pods`{{execute}} を実行して StatefulSet `nginx` の現在の Pod を確認します。

</details>

<details>
  <summary>Answer</summary>

nginx-0, nginx-1, nginx-2

</details>
