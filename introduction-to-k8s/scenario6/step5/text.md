`/root/manifests/pvc-local-path.yaml` を用意しました。  
このマニフェストファイルに必要な項目を追加して、以下の設定で PersistentVolumeClaim を作成してください。  

- PersistentVolumeClaim 名：`pvc-1`
- storageClassName: `local-path`
- サイズ：`1Gi`


<details>
  <summary>Solution</summary>

`/root/manifests/pvc-local-path.yaml` を以下のように更新します。

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-1
spec:
  storageClassName: local-path
  accessModes: 
  - ReadWriteOnce 
  resources:
    requests: 
      storage: 1Gi
```{{copy}}

`kubectl apply -f /root/manifests/pvc-local-path.yaml`{{execute}} を実行して PersistentVolumeClaim を作成します。

</details>
