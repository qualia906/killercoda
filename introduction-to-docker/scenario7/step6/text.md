作成した `docker-compose.yml` ファイルを使用して、Docker Compose でアプリケーションを detached モードでデプロイしてください。  

> **注意**  
> このラボ環境では Docker Compose のバージョンの問題で `docker compose` コマンドを使用することができません。
> かわりに従来の `docker-compose` コマンドを使用してください

デプロイが完了したら以下のリンクから `clickcounter` にアクセスしてアプリケーションが正常に動作しているか確認できます。  
{{TRAFFIC_HOST1_8085}}


<details>
  <summary>Hints</summary>

`/root/click-counter` ディレクトリに移動して `docker-compose up` コマンドを使用します。

</details>


<details>
  <summary>Solution</summary>

以下を実行します。
```
cd /root/click-counter
docker-compose up -d
```{{execute}}


アプリケーションを一括削除するには、`docker-compose down -f /root/click-counter/docker-compose.yml` を実行します。

</details>