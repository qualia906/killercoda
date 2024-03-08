いま起動したコンテナ内で `touch newfile.txt` コマンドを実行して新しいファイルを作成してください。



<details>
  <summary>Hints</summary>

`docker container exec` コマンドを使用してコンテナ内で `touch newfile.txt` を実行します。

</details>

<details>
  <summary>Solution</summary>

`docker container exec alpine-1 touch newfile.txt`{{execute}} コマンドを実行します

</details>
