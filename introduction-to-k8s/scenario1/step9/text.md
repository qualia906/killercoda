Pod `webapp` の `appsrvx` コンテナがエラー状態になっているのはなぜですか？

- [ ] このイメージのアプリケーションがエラーを起こしている
- [ ] この名前の Docker イメージが Docker Hub に存在していない
- [ ] NGINX がこのコンテナと通信するように構成されていない
- [ ] Kubernetes クラスタがエラーを起こしている

<details>
  <summary>Hints</summary>

`kubectl describe` コマンドを使用します。

</details>

<details>
  <summary>Solution</summary>

`kubectl describe pod webapp`{{execute}} を実行し、`Events` セクションを確認します。

<details>
  <summary>Answer</summary>

この名前の Docker イメージが Docker Hub に存在していない

</details>

