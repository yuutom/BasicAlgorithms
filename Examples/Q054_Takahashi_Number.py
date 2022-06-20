# 最短経路問題, BFS

from collections import deque

N, M = map(int, input().split())

# 以下はグラフの作成方法を工夫している
# グラフの要素数を N+M にして間に点を作成して総辺数を減らしている
edge = [[] for _ in range(N+M)]
for i in range(M):
    K = int(input())
    R = list(map(int, input().split()))
    for r in R:
        edge[N+i].append(r-1)
        edge[r-1].append(N+i)

INF = 10 ** 9
dist = [INF] * (N+M)
dist[0] = 0
q = deque()
q.append(0)

# 幅優先探索
while q:
    now = q.popleft()
    for to in edge[now]:
        if dist[to] != INF:
            continue
        dist[to] = dist[now] + 1
        q.append(to)

for i in range(N):
    if dist[i] == INF:
        print(-1)
    else:
        print(dist[i]//2)
