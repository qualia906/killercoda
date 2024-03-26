StorageClass `local-path` を指定して PersistentVolumeClaim を作成した場合の動作として正しいのはどれですか。

- [ ] PersistentVolumeClaim が作成されると同時に対応する PersistentVolume が作成されバインドされる。
- [ ] PersistentVolume は自動作成されず、手動で作成する必要がある。
- [ ] PersistentVolumeClaim を使用する Pod が作成される際に PersistentVolume が自動作成されバインドされる。



<details>
  <summary>Hints</summary>

以下のドキュメントを参照してください。  
https://kubernetes.io/ja/docs/concepts/storage/storage-classes/#%E3%83%9C%E3%83%AA%E3%83%A5%E3%83%BC%E3%83%A0%E3%83%90%E3%82%A4%E3%83%B3%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0%E3%83%A2%E3%83%BC%E3%83%89

</details>

<details>
  <summary>Answer</summary>
PersistentVolumeClaim が割り当てられた Pod が起動する際に PersistentVolume が自動作成されバインドされる。

</details>