`/root/playbooks/` ディレクトリの下に `question12.yaml` という yaml ファイルが用意されています。  
このファイルに以下の給与明細 (payslips) の情報を追加してください。  
住所 (address) は辞書ですが、給与明細 (payslips) は各月 (month) とその金額 (amount) を要素にした配列で記載してください。  

**payslips**  
|month|amount|
|---|---|
|june|1400|
|july|1600|
|august|2400|


<details>
  <summary>Solution</summary>

`/root/playbooks/question12.yaml` を以下の内容に更新します。
```
employee:
  name: john
  gender: male
  age: 24
  address:
    city: edison
    state: "new jersey"
    country: "united states"
  payslips:
    - month: june
      amount: 1400
    - month: july
      amount: 1600
    - month: august
      amount: 2400
```{{copy}}

</details>