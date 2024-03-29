作成したプライベート レジストリに以下の 2 つのイメージを保存してください。

- イメージ：`nginx`
- イメージ：`httpd`

レジストリのサーバー名は `localhost:5000` で指定できます。
レジストリにイメージが保存できているかは `curl -X GET localhost:5000/v2/_catalog`{{execute}} で確認できます。

> **注意**  
> まず最初に 2 つのイメージを pull する必要があります。


<details>
  <summary>Hints</summary>

- イメージを保存する前に、保存先のプライベート レジストリのサーバー名を付加した別名のイメージを `docker image tag` コマンドで作成します。
- `docker image push` コマンドを使用してイメージを保存します。

</details>

<details>
  <summary>Solution</summary>

まずイメージを `pull` します。
```
docker image pull nginx
docker image pull httpd
```{{execute}}


次に、取得したイメージから別名のイメージを作成します。
```
docker image tag nginx localhost:5000/nginx
docker image tag httpd localhost:5000/httpd
```{{execute}}


イメージをプライベート レジストリに `push` します。
```
docker image push localhost:5000/nginx
docker image push localhost:5000/httpd
```{{execute}}


</details>