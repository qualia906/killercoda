Deployment `frontend-dep` の Pod が `READY` 状態にならない原因は何ですか。

- [ ] Deployment が正常に作成されなかった
- [ ] Kubernetes クラスタに異常がある
- [ ] busybox999 というイメージが存在しない
- [ ] イメージ内のアプリケーションにいじょうがある

<details>
  <summary>Hints</summary>

`kubectl describe pod` コマンドを実行し、`Events` フィールドを確認します。

</details>

<details>
  <summary>Answer</summary>

busybox999 というイメージが存在しない

</details>
