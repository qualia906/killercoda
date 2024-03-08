`ubuntu` イメージが作成されるときに使われる Dockerfile を `/root/Dockerfile-ubuntu` として用意しました。このファイルを参照して回答してください。  
`ubuntu` イメージからコンテナが起動したとき、どのコマンドが実行されますか。

- [ ] bash
- [ ] /root bash
- [ ] ubuntu
- [ ] entrypoint bash
- [ ] bash ubuntu


<details>
  <summary>Hints</summary>

`/root/Dockerfile-ubuntu` を参照して `CMD` のアーギュメントを確認します。

</details>

<details>
  <summary>Solution</summary>

`cat /root/Dockerfile-ubuntu | grep CMD`{{exec}} を実行します。

</details>

<details>
  <summary>Answer</summary>

bash

</details>