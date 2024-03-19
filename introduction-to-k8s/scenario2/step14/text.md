`redis-definition.yaml` という名前のマニフェスト ファイルを作成し、以下の設定で Pod を作成してください。

Pod 名：redis
イメージ：redis123 (不適切なイメージ名ですがこれを指定します)


<details>
  <summary>Hints</summary>

マニフェスト ファイルを作成し、`kubectl apply` コマンドを使用して Pod を作成します。

</details>

<details>
  <summary>Solution</summary>

`kubectl run redis --image=redis123 --dry-run=client -o yaml > redis-definition.yaml`{{execute}} を実行し、`redis-definition.yaml` という名前のマニフェスト ファイルを作成します。  
`kubectl apply -f redis-definition.yaml`{{execute}} を実行し、Pod を作成します。

</details>