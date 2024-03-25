Deployment `frontend-canary` のレプリカ数を `4` にスケールアウトしてください。  

- Deployment 名：`frontend-canary`
- レプリカ数：`4`


<details>
  <summary>Hints</summary>

マニフェスト ファイルの `replicas` フィールドを変更します。  
または `kubectl scale deployment` コマンドを実行します。

</details>

<details>
  <summary>Solution</summary>

`kubectl scale deployment frontend-canary --replicas=4`{{execute}} を実行します。

</details>
