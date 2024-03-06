以下の設定で、`test-1` という名前の Docker コンテナを detached モードで実行してください。

- コンテナ名：`test-1`
- イメージ：`nginx:latest`


<details>
  <summary>Hints</summary>

> 解決/回答のためのヒントが書かれています。  

`docker container run` コマンドを使用します。

</details>

<details>
  <summary>Solution</summary>

> 解決/回答のために必要な手順が書かれています。ヒントだけではわからない場合はここを参照してください。

`docker container run -d --name test-1 nginx:latest`{{execute}} コマンドを実行します。

</details>

<br />

> 出題されたタスクを実行したら右下の [**CHECK**] ボタンをクリックします。  
> 正しくタスクが解決されていれば次の設問に進みます。  
> チェックをパスするまでトライしてください。

