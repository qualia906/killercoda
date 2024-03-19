`/root/playbooks/` ディレクトリの下に `question11.yaml` という yaml ファイルが用意されています。  
このファイルには、設問 10 で更新した内容と同じ内容が含まれています。  
以下の内容で 2 人目の従業員の情報を追加してください。

|Key/Property|Value|
|---|---|
|name|sarah|
|gender|female|
|age|28|


<details>
  <summary>Solution</summary>

`/root/playbooks/question11.yaml` を以下の内容に更新します。
```
employees:
  - name: john
    gender: male
    age: 24
  - name: sarah
    gender: female
    age: 28
```{{copy}}

</details>