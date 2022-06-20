# Union-Find, クエリ先読み

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


N = int(input())
Q = int(input())
UF = UnionFind(N)
l = [-1]*(N-1)
ans = []
for i in range(Q):
    t, x, y, v = map(int, input().split())
    if t == 0:
        UF.union(x-1, x)
        l[x-1] = v
    else:
        if UF.same(x-1, y-1):
            ans.append([x-1, y-1, v])
        else:
            ans.append([-1])

d = [0]*N
for i in range(1, N):
    if UF.same(i-1, i):
        d[i] = l[i-1] - d[i-1]

for i in range(len(ans)):
    if ans[i][0] == -1:
        print('Ambiguous')
    else:
        x, y, v = ans[i]
        if (y-x) % 2:
            print(d[y] - (v-d[x]))
        else:
            print(d[y] + (v-d[x]))