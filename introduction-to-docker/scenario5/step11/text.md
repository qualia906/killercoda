コンテナ `nginx-1` で `bash -c "echo 'My important data' > /usr/local/share/my-volume/data.txt'"` を実行してください。
これを実行することで、`my-volume` 内にファイルが書き込まれます。

<details>
  <summary>Hints</summary>

`docker container exec` コマンドを使用して `bash -c "echo 'My important data' > /usr/local/share/my-volume/data.txt'"` を実行します。

</details>

<details>
  <summary>Solution</summary>

`docker container exec nginx-1 bash -c "echo 'My important data' > /usr/local/share/my-volume/data.txt'"`{{execute}} を実行します。

</details>
