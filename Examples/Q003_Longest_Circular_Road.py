from collections import deque

N = int(input())
# 無向グラフ作成
G = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].append(b)
    G[b].append(a)


# 幅優先探索
# ある点sから各点までの距離をdistに格納
def bfs(s):
    dist = [-1] * N  # 初期化
    dist[s] = 0  # 自分自身との距離は0
    deq = deque([s])
    while deq:
        v = deq.popleft()
        for nv in G[v]:
            if dist[nv] == -1:
                deq.append(nv)
                dist[nv] = dist[v] + 1
    return dist


# 0から最も遠い点を求める
dist0 = bfs(0)
index = dist0.index(max(dist0))
# その点からさらに最も遠い点を求め、長さを直径とする
r_dist = bfs(index)
# 直径に1を加えたものが答えとなる
print(max(r_dist) + 1)