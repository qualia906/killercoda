Pod `nginx-2` の `/data/mydata.txt` 内容を表示して確認してください。   
ファイルの内容は以下のどれですか。

- [ ] ファイルの内容は空
- [ ] ファイルが存在しない
- [ ] my_data
- [ ] my_datamy_data


<details>
  <summary>Hints</summary>

`kubectl exec` コマンドを使用して Pod 内で `cat` コマンドを実行できます。  
https://kubernetes.io/docs/reference/kubectl/generated/kubectl_exec/

</details>

<details>
  <summary>Solution</summary>

`kubectl exec -it nginx-2 -- cat /data/mydata.txt`{{execute}} を実行します。

</details>

<details>
  <summary>Answer</summary>

my_data

> 削除前と同じ PersistentVolume が Pod `nginx-2` に関連付けられているためデータの利用を継続できます。

</details>
