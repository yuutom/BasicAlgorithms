# ダイクストラ法

from heapq import heappop, heappush

N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append([b, c])
    edge[b].append([a, c])


def dijk(s):
    start = [0, s]
    pq = [start]
    # dist[i] := s から i までの最短距離
    dist = [10 ** 18 for _ in range(N)]
    dist[s] = 0
    while pq:
        now = heappop(pq)
        d, pos = now
        for x in edge[pos]:
            to, cost = x
            if d + cost < dist[to]:
                dist[to] = d + cost
                heappush(pq, [dist[to], to])
    return dist


dist_from1 = dijk(0)
dist_fromN = dijk(N-1)

for k in range(N):
    # 1 から kまでの最短経路 + N から k までの最短経路
    print(dist_from1[k] + dist_fromN[k])