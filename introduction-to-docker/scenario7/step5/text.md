先ほどと同じ構成のアプリケーションを Docker Compose を使用して作成します。  
`/root/click-counter` ディレクトリに `docker-compose.yml` という名前で Compose ファイルを作成してください。  

この Compose ファイルには以下の内容が指定されている必要があります。 

- `redis` サービス設定
  - イメージ：`redis:alpine`
- `clickcounter` サービス設定
  - イメージ：`qualia906/click-counter`
  - コンテナポート：`5000`
  - ホストポート：`8085`

> 注意
> `docker-compose.yml` の先頭か末尾に `version: '3.7'` という行を入れてください。  
> これは Compose ファイルのバージョンを指定するもので、バージョンによってサポートされている設定オプションに違いがあります。  
> https://docs.docker.jp/compose/compose-file/compose-versioning.html

<br />

テキストで紹介した以下の Compose ファイルを参考に作成してください。  
https://github.com/dockersamples/example-voting-app/blob/main/docker-compose.yml


<details>
  <summary>Solution</summary>

以下の内容で `docker-compose.yml` を作成します。
```
services:
  redis:
    image: redis:alpine
  clickcounter:
    image: qualia906/click-counter
    ports:
      - 8085:5000
version: '3.7'
```{{copy}}

</details>
