作成した `docker-compose.yml` ファイルを使用して、Docker Compose でアプリケーションを detached モードでデプロイしてください。  
デプロイが完了したら以下のリンクから `clickcounter` にアクセスしてアプリケーションが正常に動作しているか確認できます。  
{{TRAFFIC_HOST1_8085}}

> 注意
> このラボ環境では Docker Compose のバージョンの問題で `docker compose` コマンドを使用することができません。
> 

(時間に余裕があれば、Docker Compose でのアプリケーションの一括削除も試してみてください)

<details>
  <summary>Hints</summary>

`docker compose up` コマンドを使用します。

</details>


<details>
  <summary>Solution</summary>

`docker compose up -d -f /root/click-counter/docker-compose.yml`{{execute}} を実行します。  
アプリケーションを一括削除するには、`docker compose down -f /root/click-counter/docker-compose.yml` を実行します。

</details>