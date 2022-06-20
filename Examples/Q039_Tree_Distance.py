import sys
sys.setrecursionlimit(10**9)

N = int(input())
# dp[x] = 頂点 x の子の頂点の個数
dp = [0] * N
edge = [[] for _ in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    edge[a].append(b)
    edge[b].append(a)


# 頂点 x の子の頂点の個数を求める
# 頂点 x の直属の子を y1, y2, …, yk とする時、
# dp[x] = dp[y1] + dp[y2] + … + dp[yk] + 1(この 1 は自分自身)
# pos は木の頂点(根)
def dfs(pos, pre):
    dp[pos] = 1
    for nv in edge[pos]:
        if nv != pre:
            dfs(nv, pos)
            dp[pos] += dp[nv]


dfs(0, -1)
ans = 0
for v in dp:
    ans += v * (N-v)

print(ans)

# 以下のようにダイクストラ法の繰り返しで求めるとTLE
# from heapq import heappop, heappush
#
# N = int(input())
# G = [[] for _ in range(N)]
# for _ in range(N-1):
#     a, b = map(int, input().split())
#     a, b = a-1, b-1
#     G[a].append(b)
#     G[b].append(a)
#
# d = []
#
#
# def dijk(s):
#     start = [0, s]
#     pq = [start]
#     # dist[i] := s から i までの最短距離
#     dist = [10 ** 18 for _ in range(N)]
#     dist[s] = 0
#     while pq:
#         now = heappop(pq)
#         d, pos = now
#         for x in G[pos]:
#             to = x
#             cost = 1
#             if d + cost < dist[to]:
#                 dist[to] = d + cost
#                 heappush(pq, [dist[to], to])
#     return dist
#
#
# ans = 0
# for i in range(N-1):
#     di = dijk(i)
#     d = di[i:]
#     ans += sum(d)
#
# print(ans)