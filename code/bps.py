from collections import deque

# グラフの隣接リストを引数にした幅優先探索
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

# input
N = int(input())
graph = []
for i in range(N):
    inpu = list(map(int,input().split()))
    graph.append(inpu[2:])

for i in range(N):
    print(i+1, bfs(graph)[i], sep=" ")
