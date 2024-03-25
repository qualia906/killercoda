Version 2 と Version 3 のアプリケーションにアクセスできるように Service `frontend-service` を更新してください。  

アクセス先が正しく切り替わったかどうかは、以下のリンクからアプリケーションにアクセスして確認できます。  
ブラウザを何度かリロードして 2 つのバージョンにアクセスできることを確認してください。  
{{TRAFFIC_HOST1_30080}}


<details>
  <summary>Hints</summary>

`/root/manifests/frontend-service.yaml` を編集して `selector` フィールドを更新します。

</details>

<details>
  <summary>Solution</summary>

`/root/manifests/frontend-service.yaml` を以下のように更新し、2 つのバージョンに共通するラベルである `name: webapp` だけを `selector` フィールドに設定します。

```
apiVersion: v1
kind: Service
metadata:
  name: frontend-service
  namespace: default
spec:
  ports:
  - nodePort: 30080
    port: 8080
    protocol: TCP
    targetPort: 8080
  selector:
    name: webapp
  type: NodePort
```{{copy}}

`kubectl apply -f /root/manifests/frontend-service.yaml`{{execute}} を実行します。

</details>
