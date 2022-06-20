# Union-Find木, クラスカル法

import heapq


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


N, M = map(int, input().split())
HQ = []
heapq.heapify(HQ)
for _ in range(M):
    c, l, r = map(int, input().split())
    heapq.heappush(HQ, (c, l, r))

UF = UnionFind(N+1)
cost = 0
while HQ:
    c, l, r = heapq.heappop(HQ)
    if UF.same(l-1, r):
        continue
    UF.union(l-1, r)
    cost += c

if len(UF) == 1:
    print(cost)
else:
    print(-1)
