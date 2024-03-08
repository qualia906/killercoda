プライベート レジストリを削除します。
コンテナ `my-registry` を削除してください。

<details>
  <summary>Hints</summary>

`docker container stop` コマンドを使用してコンテナを停止してから `docker container rm` コマンドでコンテナを削除します。

</details>

<details>
  <summary>Solution</summary>

```
docker container stop my-registry
docker container rm my-registry
```{{execute}}

</details>
