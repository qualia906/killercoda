ネットワーク `bridge` のサブネット構成は以下のどれですか。

- [ ] 172.17.0.0/16
- [ ] 182.18.0.1/16
- [ ] 192.168.0.1/24
- [ ] 172.17.0.1/24


<details>
  <summary>Hints</summary>

`docker network inspect` コマンドを使用します。

</details>

<details>
  <summary>Solution</summary>

`docker network inspect bridge`{{execute}} コマンドを実行して `Subnet` の値を確認します。

</details>

<details>
  <summary>Answer</summary>

172.17.0.0/16

</details>
