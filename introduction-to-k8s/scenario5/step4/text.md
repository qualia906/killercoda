`docker container inspect alpine-1`{{execute}} を実行してください。
そして、`GraphDriver.Data` に表示された `MergedDir` と `UpperDir` のパスをコピーしてメモしてください。

出力結果の例：
```
GraphDriver": {
  "Data": {
    "LowerDir": "/var/lib/docker/overlay2/19e49dfa0dc9f46e11ed14b4fac87a58a8d6d3f952231d331f4f376794548c5d-init/diff:/var/lib/docker/overlay2/9aba14641007d2ee4f7c1ebd88c50e3111ce86d3b35786f0adc5e78c223ccb38/diff",
    "MergedDir": "/var/lib/docker/overlay2/19e49dfa0dc9f46e11ed14b4fac87a58a8d6d3f952231d331f4f376794548c5d/merged",
    "UpperDir": "/var/lib/docker/overlay2/19e49dfa0dc9f46e11ed14b4fac87a58a8d6d3f952231d331f4f376794548c5d/diff",
    "WorkDir": "/var/lib/docker/overlay2/19e49dfa0dc9f46e11ed14b4fac87a58a8d6d3f952231d331f4f376794548c5d/work"
```