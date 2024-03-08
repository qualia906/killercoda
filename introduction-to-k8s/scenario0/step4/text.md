(※ スクリプトの実行が完了してから開始してください)  
`alpine-1` という名前のコンテナを起動しました。  
このコンテナが接続されているネットワークは以下のどれですか。

- [ ] bridge
- [ ] host
- [ ] none
- [ ] container

> 設問の中でスクリプトが実行されることがあります。  
> この場合は、スクリプトの実行が完了し **Done** が出力されてから作業を開始してください。

<details>
  <summary>Hints</summary>

`docker container inspect` コマンドを使用します。

</details>

<details>
  <summary>Solution</summary>

`docker container inspect alpine-1`{{execute}} コマンドを実行し、`Networks` セクションを確認します。

</details>

<details>
  <summary>Answer</summary>

bridge

</details>
