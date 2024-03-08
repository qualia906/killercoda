Pod `webapp` の `appsrvx` コンテナはどのような状態ですか。  
Pod の状態が ContainerCreating の場合は、その状態が終了するまで待って回答してください。

- [ ] Running
- [ ] Ready
- [ ] Succeeded
- [ ] Failed
- [ ] Waiting


<details>
  <summary>Hints</summary>

`kubectl describe` コマンドを使用します。

</details>

<details>
  <summary>Solution</summary>

`kubectl describe pod webapp`{{execute}} を実行して、コンテナ `appsrvx` の状態を確認します。

</details>

<details>
  <summary>Answer</summary>

Error or Waiting

</details>
