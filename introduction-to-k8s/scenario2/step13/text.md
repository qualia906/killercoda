次の問題では Pod のマニフェスト ファイルを作成します。  
マニフェスト ファイルを一から作成せずに済ませる Tips として、`--dry-run=client -o yaml` を使用する方法があります。
    
`kubectl run lab-1 --image nginx --dry-run=client -o yaml > lab-1.yaml`{{execute}} を実行してみてください。  
実際に Pod が作成されることはありませんが、Pod のマニフェスト ファイルが `lab-1.yaml` に出力されます。`lab-1.yaml` を開いて、Pod のマニフェスト ファイルを確認してみてください。  
  
このようにベースとなるマニフェスト ファイルを作成して必要なプロパティを追加・削除することで、一から書かずにマニフェスト ファイルを作成することができます。  
この方法は Pod だけでなく Deployment などの他のリソースでも使用できます。  
  
また、すでに作成済みの Pod がある場合は、`kubectl get pod POD_NAME -o yaml > pod.yaml` を実行して、Pod のマニフェスト ファイルを作成することもできます。