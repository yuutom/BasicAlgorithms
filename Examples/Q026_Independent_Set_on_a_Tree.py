# 木 : 連結で閉路を持たない(無向)グラフ
# 連結 : グラフ G の任意の二頂点 u,v ∈ V に対して、u−v パスまたは v−u パスが存在するとき、G は連結
# 閉路 : 路のうち、始点と終点が等しいものをサイクル(閉路)という
# ２部グラフ：辺で直接結ばれた頂点同士が互いに違う色となるように2色で塗ることが出来るグラフ
# 木は２部グラフである

import sys

sys.setrecursionlimit(10**6)
N = int(input())
G = [[] for _ in range(N)]
# colors[i] = 頂点 i の色
colors = [-1] * N
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)


# 二色に塗り分けをする
# どちらかの数は必ず N//2 より多くなるので、それを答えにする
def dfs(pos, color):
    colors[pos] = color
    for i in G[pos]:
        if colors[i] == -1:
            # 一つ先に進むごとに 0, 1, 0, 1 … と塗り分ける
            dfs(i, abs(color-1))


dfs(0, 0)

# enumerate(リスト) : リストのインデックスと要素を同時に取り出す
# ans = color == 0 の index を格納するリスト
ans = [index for index, color in enumerate(colors) if color == 0]
if len(ans) < N // 2:
    ans = [index for index, color in enumerate(colors) if color == 1]

for i in range(len(ans)):
    ans[i] += 1

print(*ans[0:N//2])
