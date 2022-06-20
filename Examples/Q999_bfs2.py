# bfs
# https://atcoder.jp/contests/abc224/tasks/abc224_d

from collections import deque

M = int(input())
edge = [[] for _ in range(9)]
for _ in range(M):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    edge[u].append(v)
    edge[v].append(u)

P = [8]*9
for i, p in enumerate(map(int, input().split())):
    P[p-1] = i

P = tuple(P)
D = dict({P:0})
que = deque([P])
while que:
    p = que.popleft()
    l = list(p)
    v = l.index(8)
    for u in edge[v]:
        l[u], l[v] = l[v], l[u]
        q = tuple(l)
        if q not in D:
            que.append(q)
            D[q] = D[p]+1
        l[u], l[v] = l[v], l[u]

goal = tuple(range(9))
print(D[goal] if goal in D else -1)