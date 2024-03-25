Version 1 のアプリケーションにアクセスするための Serive `frontend-service` は `/root/manifests/frontend-service.yaml` で定義されています。  
いま作成した `frontend-green` の Version 2 のアプリケーションにアクセス先が切り替わるように `frontend-service` を更新してください。  

アクセス先が正しく切り替わったかどうかは、以下のリンクからアプリケーションにアクセスして確認できます。  
{{TRAFFIC_HOST1_30080}}


<details>
  <summary>Hints</summary>

`/root/manifests/frontend-service.yaml` を編集して `selector` フィールドを更新します。

</details>

<details>
  <summary>Solution</summary>

`/root/manifests/frontend-service.yaml` を以下のように更新します。

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
    version: v2
  type: NodePort
```{{copy}}

`kubectl apply -f /root/manifests/frontend-service.yaml`{{execute}} を実行します。

</details>
