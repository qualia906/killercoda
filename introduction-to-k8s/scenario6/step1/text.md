`/root/manifests/pod-emptydir.yaml` を用意しました。  
このマニフェスト ファイルに必要な項目を追加して、以下の設定で Volume をマウントした Pod を作成してください。

- Pod 名：`pod-emptydir`
- イメージ：`nginx`
- Volume タイプ：`EmptyDir`
- Volume 名：`cache-volume`
- マウントパス：`/cache`


<details>
  <summary>Solution</summary>

`/root/manifests/pod-emptydir.yaml` を以下のように更新します。

```
apiVersion: v1
kind: Pod
metadata:
  name: pod-emptydir
spec:
  containers:
    - name: nginx-container
      image: nginx
      volumeMounts:
        - mountPath: /cache
          name: cache-volume
  volumes:
    - name: cache-volume
      emptyDir: {}
```{{copy}}

`kubectl apply -f /root/manifests/pod-emptydir.yaml` を実行して Pod を作成します。

</details>