import sys
sys.setrecursionlimit(10**8)

N, Q = map(int, input().split())
X = list(map(int, input().split()))
edge = [[] for _ in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    edge[a].append(b)
    edge[b].append(a)

visited = [False] * N
P = [[] for i in range(N)]


def dfs(i):
    visited[i] = True
    P[i] = [X[i]]
    for x in edge[i]:
        if not visited[x]:
            dfs(x)
            P[i].extend(P[x])
    P[i].sort(reverse=True)
    if len(P[i]) > 20:
        P[i] = P[i][:20]


dfs(0)
for _ in range(Q):
    v, k = map(int, input().split())
    v, k = v-1, k-1
    print(P[v][k])
