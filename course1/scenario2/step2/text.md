https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#scaling-a-deployment

`my-first-deployment` のレプリカ数を ３ にスケールアウトしなさい。


<br>
<details><summary>Solution</summary>
<br>
  
```plain
k scale deployment/my-first-deployment --replicas=3

k get deployment my-first-deployment
```{{exec}}

</details>
