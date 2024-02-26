このホストからすべてのコンテナを削除してください。  
起動中および停止中のすべてのコンテナを削除します。必要に応じて削除前にコンテナを停止してください。

<details>
  <summary>Hints</summary>

コンテナを停止するには `docker container stop <CONTAINER ID | CONTAINER NAME>` コマンドを実行します。  
コンテナを削除するには `docker container rm <CONTAINER ID | CONTAINER NAME>` コマンドを実行します。

</details>

<details>
  <summary>Solution</summary>

すべてのコンテナを一括で停止するには `docker container stop $(docker ps -aq)` を実行します。  
すべてのコンテナを一括で削除するには `docker container rm $(docker ps -aq)` コマンドを実行します。

</details>