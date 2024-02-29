実行したコンテナの OS バージョンは何ですか。 
OS バージョンは、コンテナ内の /etc/os-release ファイルを参照することで調べることができます。

- [ ] 4.2.1
- [ ] 1.2.4
- [ ] 3.9.3
- [ ] 2.6.1
- [ ] 1.8.0

<details>
  <summary>Hints</summary>

`docker container exec` コマンドを使用してコンテナ内の /etc/os-release を参照します。

</details>

<details>
  <summary>Solution</summary>

`docker container exec webapp cat /etc/os-release`{{execute}} を実行してバージョンを確認します。

</details>

<details>
  <summary>Answer</summary>

3.9.3

</details>