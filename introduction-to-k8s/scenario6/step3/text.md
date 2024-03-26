StorageClass `local-path` の volumeBindingMode は何ですか。

- [ ] Immediate
- [ ] WaitForFirstConsumer
- [ ] Manual
- [ ] WaitForFirstCreator


<details>
  <summary>Hints</summary>

`kubectl get sc` コマンドまたは `kubectl describe sc` コマンドを使用します。

</details>

<details>
  <summary>Solution</summary>

`kubectl get sc`{{execute}} コマンドを実行して `VOLUMEBINDINGMODE` 列を確認します。

</details>

<details>
  <summary>Answer</summary>

WaitForFirstConsumer

</details>
