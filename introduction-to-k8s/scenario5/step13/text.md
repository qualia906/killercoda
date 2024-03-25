続いて、カナリアリリースで新しいバージョン (Version 3) のアプリケーションをデプロイします。  
以下の設定で新しい Deployment を作成してください。

- Deployment 名：`frontend-canary`
- イメージ：`qualia906/webapp-color:v3`
- レプリカ数：`1`
- Pod のラベル：`name=webapp`, `version=v3` (`matchLabels` にも注意してください)
- containerPort：`8080`
- protocol：`TCP`


<details>
  <summary>Hints</summary>

`/root/manifests/frontend-definition.yaml` をコピーして使用して構いません。

</details>

<details>
  <summary>Solution</summary>

`/root/manifests/frontend-definition.yaml` をコピーして、例えば、`/root/manifests/frontend-canary.yaml` という名前で以下の内容のマニフェスト ファイルを作成します。

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend-canary
  namespace: default
spec:
  replicas: 1
  revisionHistoryLimit: 10
  selector:
    matchLabels:
      name: webapp
      version: v3
  strategy:
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 25%
    type: RollingUpdate
  template:
    metadata:
      creationTimestamp: null
      labels:
        name: webapp
        version: v3
    spec:
      containers:
      - image: kodekloud/webapp-color:v3
        imagePullPolicy: IfNotPresent
        name: simple-webapp
        ports:
        - containerPort: 8080
          protocol: TCP
        resources: {}
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
      dnsPolicy: ClusterFirst
      restartPolicy: Always
      schedulerName: default-scheduler
      securityContext: {}
      terminationGracePeriodSeconds: 30
```{{copy}}

`kubectl apply -f frontend-green.yaml`{{execute}} を実行して Deployment を作成します。

</details>