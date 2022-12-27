https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#scaling-a-deployment

`my-first-deployment` のレプリカ数を ２ にスケールインしなさい。


<br>
<details><summary>Solution</summary>
<br>

```plain
k scale deployment/my-first-deployment --replicas=2

k get deployment my-first-deployment
```{{exec}}

</details>
