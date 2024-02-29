この `Dockerfile` を使用し、`color-webapp` という名前をつけてイメージをビルドしてください。タグは指定しないでください。

- イメージ名：`color-webapp`

<details>
  <summary>Hints</summary>

`docker image build` コマンドを使用します。`-t` オプションでイメージ名を指定します。  
コマンドを実行するために適切なディレクトリに移動することを忘れないようにしてください。

</details>

<details>
  <summary>Solution</summary>

以下を実行します。

```
cd /root/color-webapp
docker image build -t color-webapp .
```{{execute}}

</details>