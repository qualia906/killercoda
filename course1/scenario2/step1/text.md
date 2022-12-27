https://kubernetes.io/docs/concepts/workloads/controllers/deployment/

下記要件の Deployment を default 名前空間に作成し、正常に実行されていることを確認しなさい。

名前：　`my-first-deployment`  
イメージ： `nginx:alpine`


<br>
<details><summary>Solution</summary>
<br>

```plain
k create deployment my-first-deployment --image=nginx:alpine
k get deployment my-first-deployment
```{{exec}}
</details>
