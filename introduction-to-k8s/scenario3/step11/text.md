`/root/manifests/` ディレクトリ以下にマニフェスト ファイル `deployment-definition-1.yaml` を用意しました。  
ただし、この `deployment-definition-1.yaml` にはいくつかの誤りが含まれています。  
誤りを修正した上で、このマニフェスト ファイルを使用して正常に実行される Deployment を作成してください。

- Deployment 名：deploy-1


<details>
  <summary>Hints</summary>

誤りを含んだマニフェスト ファイルを使用して Deployment を作成しようとする際に表示されるエラーメッセージから、誤りの内容を推測することができます。  
マニフェスト ファイルから Deployment などのオブジェクトを作成する場合には `kubectl apply -f` コマンドを使用します。

</details>

<details>
  <summary>Solution</summary>

`deployment-definition-1.yaml` の `kind` と `image` を修正し以下のように更新します。

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deployment-1
spec:
  replicas: 2
  selector:
    matchLabels:
      name: busybox-pod
  template:
    metadata:
      labels:
        name: busybox-pod
    spec:
      containers:
      - name: busybox-container
        image: busybox
        command:
        - sh
        - "-c"
        - echo Hello Kubernetes! && sleep 3600

```

更新したら `kubectl apply -f /root/manifests/deployment-definition-1.yaml`{{execute}} を実行します。

</details>