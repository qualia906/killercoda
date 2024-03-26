`/root/manifests/deployment-definition.yaml` を用意しました。  
このマニフェスト ファイルに必要な項目を追加して、以下の設定で Deployment を作成してください。

- Deployment 名：`test-2`
- イメージ：`nginx`
- レプリカ数：`2`

> ラボの中で YAML ファイルを編集することがあります。  
> この時、**Editor** を使用することができます。vi や nano を使用しても構いません。 

<details>
  <summary>Solution</summary>

`/root/manifests/deployment-definition.yaml` を以下のように更新します。

```
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: test-2
  name: test-2
spec:
  replicas: 2
  selector:
    matchLabels:
      app: test-2
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: test-2
    spec:
      containers:
      - image: nginx
        name: nginx
        resources: {}
status: {}
```{{copy}}

`kubectl apply -f /root/manifests/deployment-definition.yaml`{{execute}} コマンドを実行します。

</details>

<br />

> 出題されたタスクを実行したら右下の [**CHECK**] ボタンをクリックします。  
> 正しくタスクが解決されていれば次の設問に進みます。  
> チェックをパスするまでトライしてください。

