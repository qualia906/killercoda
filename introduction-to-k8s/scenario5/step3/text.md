Deployment `frontend` で使用されているコンテナイメージはどれですか。

- [ ] webapp
- [ ] frontend
- [ ] qualia906/webapp-color:v2
- [ ] qualia906/webapp-color:v1
- [ ] simple-webapp


<details>
  <summary>Hints</summary>

`kubectl describe deployment` コマンドを使用して、使われているイメージを確認します。

</details>

<details>
  <summary>Solution</summary>

`kubectl describe deployment frontend | grep Image`{{execute}} コマンドを実行します。

</details>

<details>
  <summary>Answer</summary>

qualia906/webapp-color:v1

</details>
