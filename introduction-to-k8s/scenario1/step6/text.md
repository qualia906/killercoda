(※ スクリプトの実行が完了してから開始してください)  
新しく `webapp` という Pod を作成しました。この Pod はいくつのコンテナで構成されていますか？  
今のところ Pod の状態は無視して構いません。

- [ ] 3
- [ ] 2
- [ ] 1
- [ ] 0

<details>
  <summary>Hints</summary>

`kubectl get pod` コマンドか `kubectl describe pod` コマンドを使用します。

</details>

<details>
  <summary>Solution</summary>

`kubectl get pod webapp`{{execute}} を実行して `READY` 列を確認します。
あるいは、`kubectl describe pod webapp`{{execute}} を実行して `Containers` セクションを確認します。

</details>

<details>
  <summary>Answer</summary>

2

</details>
