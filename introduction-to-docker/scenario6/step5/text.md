以下の設定で新しいネットワークを作成してください。

- ネットワーク名：`mysql-network`
- ドライバー：`bridge`
- サブネット：`182.18.0.1/24`
- ゲートウェイ：`182.18.0.1`


<details>
  <summary>Hints</summary>

- ネットワークを作成するには `docker network create` コマンドを使用します。
- ドライバーを設定するには `--driver` フラグを指定します。
- サブネットを設定するには `--subnet` フラグを指定します。
- ゲートウェイを設定するには `--gateway` フラグを指定します。
https://matsuand.github.io/docs.docker.jp.onthefly/engine/reference/commandline/network_create/

</details>

<details>
  <summary>Solution</summary>

`docker network create --driver bridge --subnet 182.18.0.1/24 --gateway 182.18.0.1 mysql-network`{{execute}} コマンドを実行します。

</details>