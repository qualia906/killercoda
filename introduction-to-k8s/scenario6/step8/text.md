PersistentVolueClaim `pvc-1` の STATUS はどうなっていますか。

- [ ] Bound
- [ ] Unbound
- [ ] Pending
- [ ] Failed

<details>
  <summary>Hints</summary>

`kubectl get pvc` コマンドを使用します。

</details>


<details>
  <summary>Solution</summary>

`kubectl get pvc`{{execute}} を実行して `STATUS` 列を確認します。  

</details>

<details>
  <summary>Answer</summary>

Bound

> この PersistentVolumeClaim を使用した Pod が作成された際に PersistentVolume が作成され、PersistentVolumeClaim にバインドされました。

</details>