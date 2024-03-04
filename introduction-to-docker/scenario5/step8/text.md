再度、先ほどコピーしたパスを使用して以下のコマンドを実行してください。

```
ls -la <UpperDir のパス>
```

コンテナが削除されたためレイヤーのデータも削除され、ファイルにアクセスできないことを確認します。  


出力の例：
```
ls: cannot access '/var/lib/docker/overlay2/5b63e7a482bbe07ec5dcf69b55eb834324951bb9fafcbb4706ebc640795e79e2/diff/': No such file or directory
```