`/root/playbooks/` ディレクトリの下に `question9.yaml` という yaml ファイルが用意されています。  
このファイルに `apple` `orange` `banana` についての情報を辞書の配列として保存します。  
`apple` と同じように `orange` と `banana` について以下の情報を追加してください。

|orage||
|---|---|
|color|orange|
|weight|90g|

|banana||
|---|---|
|color|yellow|
|weight|150g|


<details>
  <summary>Solution</summary>

`/root/playbooks/question9.yaml` を以下の内容に更新します。
```
- name: apple
  color: red
  weight: 100g
- name: orange
  color: orange
  weight: 90g
- name: banana
  color: yellow
  weight: 150g
```{{copy}}

</details>
