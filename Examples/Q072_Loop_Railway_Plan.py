import sys
sys.setrecursionlimit(10**7)


class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納。
        # par[x]<0の時そのノードは根で、par[x]の絶対値はグループのサイズ
        self.parents = [-1] * n
        self.length = n

    # 親の親の...を辿って根を見つける
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            # 再度検索する時に手間がかからないよう根を繋ぎかえる
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # xの属するグループとyの属するグループを併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.length -= 1
        return True

    # 同じ集合に属するか判定
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # xが属するグループのサイズを返す
    def size(self, x):
        x = self.find(x)
        return -self.parents[x]

    # treeの数を返す
    def __len__(self):
        return self.length


AROUND = [(1, 0), (0, 1), (-1, 0), (0, -1)]
H, W = map(int, input().split())
c = [list(input()) for _ in range(H)]
used = [[False] * W for _ in range(H)]


# dfs
# sx, sy : 始点の座標
# cx, cy : 移動後の座標
def dfs(sx, sy, cx, cy):
    # 移動後の座標が始点の場合
    if sx == cx and sy == cy and used[cx][cy]:
        # 処理を終わらせて ret を更新
        return 0
    used[cx][cy] = True

    ret = -1001001001
    for dx, dy in AROUND:
        nx, ny = cx+dx, cy+dy
        # 行き先がエリア外 or 山
        if nx<0 or H<=nx or ny<0 or W<=ny or c[nx][ny]=='#':
            # for 文の最初からやり直し
            continue
        # 行き先が既に訪れた場所の場合
        if used[nx][ny]:
            # 行き先が始点じゃない場合
            if sx != nx or sy != ny:
                continue
        v = dfs(sx, sy, nx, ny)
        ret = max(ret, v+1)
    used[cx][cy] = False
    return ret


ans = -1
for i in range(H):
    for j in range(W):
        ans = max(ans, dfs(i, j, i, j))

if ans <= 2:
    print(-1)
else:
    print(ans)



