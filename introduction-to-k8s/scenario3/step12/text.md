`/root/manifests/` 以下に `deployment-definition-2.yaml` を作成して、以下の設定の Deployment を作成してください。

- Deployment 名: `deployment-2`
- イメージ: `httpd:2.4-alpine`
- レプリカ数: 3

<details>
  <summary>Hints</summary>

前の問題で使用した `deployment-definition-1.yaml` をコピーして必要な変更を加えることでマニフェスト ファイルを作成できます。  
または、`kubectl create deployment deploy-2 --image httpd:2.4-alpine --replicas 3 --dry-run=client -o yaml > /root/manifests/deployment-definition-2.yaml` コマンドを使用してマニフェスト ファイルを作成することもできます。

</details>

<details>
  <summary>Solution</summary>

`deployment-definition-2.yaml` を以下の内容で作成します。

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: httpd-frontend
spec:
  replicas: 3
  selector:
    matchLabels:
      name: httpd-frontend
  template:
    metadata:
      labels:
        name: httpd-frontend
    spec:
      containers:
      - name: httpd-frontend
        image: httpd:2.4-alpine
```

`kubectl apply -f /root/manifests/deployment-definition-2.yaml`{{execute}} を実行します。

</details>