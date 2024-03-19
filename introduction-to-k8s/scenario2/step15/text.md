いま作成した Pod `redis` のイメージを `redis` に変更してください。  
(イメージを変更して Pod が running 状態になることを確認してください)

Pod 名：redis
イメージ：redis


<details>
  <summary>Hints</summary>

Pod のマニフェスト ファイルを更新して `kubectl apply` コマンドを使用するか、`kubectl edit` コマンドを使用します。

</details>

<details>
  <summary>Solution</summary>

`kubectl edit pod redis`{{execute}} を実行してイメージを `redis` に変更します。  
または、`redis-definition.yaml` でイメージを `redis` に変更し、`kubectl apply -f redis-definition.yaml`{{execute}} を実行します。

</details>