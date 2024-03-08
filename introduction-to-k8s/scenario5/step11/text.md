コンテナ `nginx-1` の `/usr/local/share/my-volume` に `data.txt` というファイルを作成して `My important data` という文字列を保存してください。これを実行することで、`my-volume` 内にファイルが保存されます。

コンテナ `nginx-1` で `bash -c "echo 'My important data' > /usr/local/share/my-volume/data.txt'"` を実行してください。
これを実行することで、`my-volume` 内にファイルが書き込まれます。

<details>
  <summary>Hints</summary>

- ワンライナーで実行するには、`docker container exec` コマンドを使用して `bash -c "echo 'My important data' > /usr/local/share/my-volume/data.txt"` を実行します。
- `docker container exec -it nginx-1 bash` でコンテナのシェルにアクセスし、`echo 'My important data' > /usr/local/share/my-volume/data.txt` を実行することもできます。

</details>

<details>
  <summary>Solution</summary>

`docker container exec nginx-1 bash -c "echo 'My important data' > /usr/local/share/my-volume/data.txt"`{{execute}} を実行します。

</details>
