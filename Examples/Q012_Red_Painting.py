# Union-Find木 問題
import sys

# 再帰回数の上限を設定
sys.setrecursionlimit(10**7)
H, W = map(int, input().split())
Q = int(input())
# マス目
B = [[0] * (W + 2) for _ in range(H + 2)]
# 各要素の親要素の番号を格納するリスト
# 要素が根の場合は-(そのグループの要素数)を格納する
par = [-1] * ((H+1)*(W+1))


# find(x) = 要素 x が属するグループの親（根）を返す
# 自分が親である時は自分の番号を返し、それ以外の場合はもう一度 find を行い親を探す
# find(x) == find(y) → x, y は連結されている
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


# x,y を連結
# それぞれの親を確認し、異なる場合のみ親を統一
def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    # x の要素数を 1 増やす（-2 とする）
    par[x] += par[y]
    # y の根を x とする
    par[y] = x


for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        r, c = query[1], query[2]
        B[r][c] = 1
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            # B[r+dx][c+dy] = 1（赤マス） であれば if 実行
            if B[r+dx][c+dy]:
                # par の index が一意に決まる（?）
                unite(r * W + c, (r + dx) * W + (c + dy))
    elif query[0] == 2:
        ra, ca, rb, cb = query[1:]
        if B[ra][ca] and B[rb][cb] and find(ra*W+ca) == find(rb*W+cb):
            print('Yes')
        else:
            print('No')
