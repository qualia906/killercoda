コンテナ `nginx-2` で `cat /usr/local/share/my-volume/data.txt` を実行してください。
コンテナ `nginx-1` で保存したデータは残っていますか。

- [ ] 残っている
- [ ] 残っていない


<details>
  <summary>Solution</summary>

`docker container exec nginx-2 cat /usr/local/share/my-volume/data.txt`{{execute}} を実行します。

</details>

<details>
  <summary>Answer</summary>

残っている

</details>
