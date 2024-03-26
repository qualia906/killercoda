いま作成した `pvc-1` を使用して PersistentVolume を利用する Pod を作成します。  

`/root/manifests/pod-pv.yaml` を用意しました。  
このマニフェスト ファイルに必要な項目を追加して、PersistentVolume をマウントした Pod を作成してください。  

- Pod 名：`pod-pv`
- イメージ：`nginx`
- 使用する PersistentVolume：`pvc-1`
- Volume 名：`data-volume`
- マウントパス：`/var/www/html`


<details>
  <summary>Solution</summary>

```
apiVersion: v1
kind: Pod
metadata:
  name: pod-pv
spec:
  containers:
    - name: frontend
      image: nginx
      volumeMounts:
        - mountPath: "/var/www/html"
          name: data-volume
  volumes:
    - name: data-volume
      persistentVolumeClaim:
        claimName: pvc-1
```

</details>