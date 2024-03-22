Deployment `webapp` の Pod で使用されているイメージは何ですか。

- [ ] nginx
- [ ] httpd:2.4-alpine
- [ ] qualia906/simple-webapp:red
- [ ] localhost:5000/httpd


<details>
  <summary>Hints</summary>

`kubectl describe deployment` コマンドを使用します。  

</details>

<details>
  <summary>Solution</summary>

`kubectl describe deployment webapp`{{execute}} コマンドを実行して `Image` フィールドを確認します。  

</details>

<details>
  <summary>Answer</summary>

qualia906/simple-webapp:red

</details>