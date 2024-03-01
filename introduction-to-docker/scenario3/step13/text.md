作成した color-webapp のイメージはサイズが大きすぎます。コンテナイメージはなるべくサイズが小さく軽量な方がよいため、より小さいサイズでイメージを再作成します。
`/root/color-webapp/Dockerfile` を修正し、ベースイメージを `Python3.6` のより小さいサイズのイメージに変更して、以下の設定・要件で新しいイメージをビルドしてください。

- イメージ名：`color-webapp`
- タグ：`lite`
- イメージサイズ：`150MB` 未満

イメージは以下の Docker Hub のページから探すことができます。
https://hub.docker.com/_/python/tags?page=1&name=3.6

<details>
  <summary>Hints</summary>

- `/root/color-webapp/Dockerfile` を `vi` や `nano` エディタを使用して開きます。
- `FROM` のアーギュメントを、例えば `python:3.6-alpine` に変更します。
- `docker image build` コマンドを使用して新しいイメージをビルドします。

</details>

<details>
  <summary>Solution</summary>

Dockerfile を修正した後、`/root/color-webapp` ディレクトリで `docker image build -t color-webapp:lite .`{{exec}} を実行します。

</details>
