コンテナ `alpine-1` を削除してください。


<details>
  <summary>Hints</summary>

まず `docker container stop` でコンテナを停止します。
そして `docker container rm` でコンテナを削除します。

</details>


<details>
  <summary>Solution</summary>

以下を実行します。

```
docker container stop alpine-1
docker container rm alpine-1
```{{execute}}

</details>