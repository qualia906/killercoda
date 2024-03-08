コンテナ `redis` と `clickcounter` を削除してください。

<details>
  <summary>Solution</summary>

以下を実行します。
```
docker container stop $(docker container ls -aq)
docker container rm $(docker container ls -aq)
```{{execute}}

</details>