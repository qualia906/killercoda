`/root/playbooks/` ディレクトリの下に `question10.yaml` という yaml ファイルが用意されています。  
このファイルに複数の従業員情報を記録できるようにしたいです。  
`employee` という名前の辞書を、`employees` (複数形) という名前の配列に書き直してください。

<details>
  <summary>Solution</summary>

`/root/playbooks/question10.yaml` を以下の内容に更新します。
```
employees:
  - name: john
    gender: male
    age: 24
```{{copy}}

</details>