`/root/manifests` ディレクトリ下に `service-definition-1.yaml` を用意しました。  
このマニフェスト ファイルを使用して、Deployment `webapp` のアプリケーションにアクセスするための Service を作成します。  

ただし、このマニフェスト ファイルは不完全です。  
以下の情報に基づいてマニフェスト ファイルを修正した上で Service を作成してください。

- Service 名：`webapp-service`
- type: `NodePort`
- targetPort: `8080`
- port: `8080`
- nodePort: `30080`
- selector: Deployment `webapp` (あるいは Pod) の `Labels` を参照します


<details>
  <summary>Solution</summary>

`/root/manifests/service-definition-1.yaml` を以下のように更新します。  

```
apiVersion: v1
kind: Service
metadata:
  name: webapp-service
  namespace: default
spec:
  ports:
  - nodePort: 30080
    port: 8080
    targetPort: 8080
  selector:
    app: webapp
  type: NodePort
```{{copy}}

`kubectl apply -f /root/manifests/service-definition-1.yaml` を実行して Service を作成します。

</details>
