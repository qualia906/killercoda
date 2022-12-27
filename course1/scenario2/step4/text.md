https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#scaling-a-deployment

`my-first-deployment` で使用するイメージを `nginx:alpine` から `httpd:alpine` に変更しなさい。


<br>
<details><summary>Solution</summary>
<br>

```plain
k set image deployment my-first-deployment nginx=httpd:alpine

k get deployment my-first-deployment
```{{exec}}

</details>
