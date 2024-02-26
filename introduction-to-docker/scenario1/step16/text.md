このホストからすべてのコンテナ イメージを削除してください。  
必要に応じてコンテナも削除してください。

<details>
  <summary>Hints</summary>

イメージを削除するには `docker image rm` コマンドか `docker rmi` コマンドを使用します。

</details>

<details>
  <summary>Solution</summary>

すべてのコンテナを停止し削除します。
その上で、`docker image rm $(docker image ls -aq)` コマンドを実行してすべてのイメージを削除します。

</details>
