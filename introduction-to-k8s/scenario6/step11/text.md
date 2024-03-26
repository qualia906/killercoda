StatefulSet `nginx` の Pod である `nginx-2` の `/data/mydata.txt` に `my_data` という文字列を保存してください。


<details>
  <summary>Hints</summary>

`kubectl exec` コマンドを使用します。  
https://cloud.google.com/migrate/containers/docs/troubleshooting/executing-shell-commands?hl=ja  
https://kubernetes.io/docs/reference/kubectl/generated/kubectl_exec/

</details>

<details>
  <summary>Solution</summary>

`kubectl exec -it nginx-2 -- bash -c "echo my_data > /data/mydata.txt"`{{execute}} を実行します。  
`kubectl exec -it nginx-2 -- cat /data/mydata.txt`{{execute}} を実行して、ファイルに `my_data` が書き込まれたことを確認します。

</details>
