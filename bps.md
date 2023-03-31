# 幅優先探索
幅優先探索の結果を返します。<br>
該当頂点にたどり着けない場合は`-1`を返します。

計算量

入力形式
>

```python:bps.py
from collections import deque

#隣接リストを入力すると、幅優先探索の結果を返す
def bfs(graph):
    dist = [-1]*(len(graph))  
    #訪問予定のキューに最初の頂点を追加
    que = deque([0])
    dist[0] = 0

    while que:
        i = que.popleft()
   
        for k in graph[i]:
            if dist[k-1] == -1:
                que.append(k-1)
                dist[k-1] = dist[i] + 1 

    return dist

#input
N = int(input())
graph = []
for i in range(N):
    inpu = list(map(int,input().split()))
    graph.append(inpu[2:])

for i in range(N):
    print(i+1, bfs(graph)[i], sep=" ")
```


下記リンクの問題で、実装が正しいか確認することができます。<br>
>[AOJ-ALDS1-11-C](https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C)
