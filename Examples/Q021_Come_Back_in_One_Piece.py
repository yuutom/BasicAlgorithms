import sys
sys.setrecursionlimit(10**8)

N, M = map(int, input().split())
# 順方向の有向グラフ
G = [[] for _ in range(N)]
# 逆方向の有向グラフ
rG = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    rG[b].append(a)


# 強連結成分分解(SCC)
# ステップ① : dfsをして番号を記録
# ステップ② : 枝を逆向きにした有向グラフでdfsをする
def scc(N ,G, rG):
    order = []
    used = [0] * N
    group = [0] * N

    def dfs(s):
        # s を訪問済みにする
        used[s] = 1
        for t in G[s]:
            # t が探索済みだったらスルー
            if not used[t]:
                dfs(t)
        order.append(s)

    def rdfs(s, label):
        # s を訪問済みにする
        used[s] = 1
        # s のグループ番号は label
        group[s] = label
        for t in rG[s]:
            # t が探索済みだったらスルー
            if not used[t]:
                rdfs(t, label)

    # ステップ①
    for i in range(N):
        if not used[i]:
            dfs(i)
    # ステップ②の為に used を初期化
    used = [0] * N
    # グループ番号を定義
    label = 0
    # ステップ②
    for i in reversed(order):
        if not used[i]:
            rdfs(i, label)
            label += 1
    return label, group


def calc(label, group):
    l = [0] * label
    # それぞれの group に何個頂点があるか
    for i in group:
        l[i] += 1
    ans = 0
    for j in l:
        ans += j * (j-1) // 2
    return ans


label, group = scc(N, G, rG)
print(calc(label, group))