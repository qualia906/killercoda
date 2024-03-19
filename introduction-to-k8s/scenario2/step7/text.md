`/root/playbooks/` ディレクトリの下に `question7.yaml` という yaml ファイルが用意されています。  
このファイルの従業員情報に、`name` や `gender` 以外に以下の情報を保存するように、`address` という辞書を追加してください。

|Key/Property|Value|
|---|---|
|city|shinjuku|
|prefecture|tokyo|
|country|japan|

<details>
  <summary>Solution</summary>

`/root/playbooks/question7.yaml` を以下の内容に更新します。
```
employee:
  name: john
  gender: male
  age: 24
  address:
    city: shinjuku
    state: tokyo
    country: japan
```{{copy}}

</details>