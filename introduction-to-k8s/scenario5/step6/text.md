Deployment `frontend` のコンテナイメージを `qualia906/webapp-color:v2` にアップデートしてください。  
この Deployment は `/root/manifests/frontend-deployment.yaml` を使って定義されています。
Deployment を削除して再作成はせずに、現在の Deploeyment のコンテナイメージだけを更新してください。  

また、`Labels` は変更しないでください。

- イメージ： `qualia906/webapp-color:v2`

<details>
  <summary>Hints</summary>

`/root/manifests/frontend-deployment.yaml` を編集してイメージの設定を更新します。

</details>

<details>
  <summary>Solution</summary>

`/root/manifests/frontend-deployment.yaml` を編集して `image` フィールドを `qualia906/webapp-color:v2` に更新します。  
`kubectl apply -f /root/manifests/frontend-deployment.yaml`{{execute}} を実行します。

</details>
