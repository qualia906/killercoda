以下の設定で、再度 `my-volime` をマウントしたコンテナを detached モードで起動してください。

- イメージ名：`nginx:latest`
- コンテナ名：`nginx-2`
- マウントパス：`/usr/local/share/my-volume`


<details>
  <summary>Hints</summary>

`docker container run` で `-v my-volume:/usr/local/share/my-volume` を指定します。

</details>

<details>
  <summary>Solution</summary>

`docker container run -d --name nginx-2 -v my-volume:/usr/local/share/my-volume nginx:latest`{{execute}} を実行します。

</details>
