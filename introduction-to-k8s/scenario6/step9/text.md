`/root/manifests/statefulset-nginx.yaml` を用意しました。  
このマニフェスト ファイルに必要な項目を追加して、以下の設定で StatefulSet を作成してください。

- StatefulSet 名：`nginx`
- イメージ：`nginx:latest`
- レプリカ数：`3`
- マウントパス：`/data`
- StorageClass：`local-path`
- ストレージサイズ：`50Mi`


<details>
  <summary>Solution</summary>

`/root/manifests/statefulset-nginx.yaml` を以下の内容に更新します。

```
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: nginx
spec:
  selector:
    matchLabels:
      app: backend
  serviceName: nginx-h
  replicas: 3 
  template:
    metadata:
      labels:
        app: backend
    spec:
        containers:
          - name: nginx
            image: nginx:latest
            ports:
              - containerPort: 8080
                name: nginx
            volumeMounts:
              - name: data
                mountPath: /data
  volumeClaimTemplates:
    - metadata:
        name: data
      spec:
        accessModes: [ "ReadWriteOnce" ]
        storageClassName: local-path
        resources:
          requests:
            storage: 50Mi
```{{copy}}

`kubectl apply -f /root/manifests/statefulset-nginx.yaml`{{execute}} を実行します。

</details>
