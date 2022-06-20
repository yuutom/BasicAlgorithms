# 区間スケジューリング問題
# https://atcoder.jp/contests/keyence2020/tasks/keyence2020_b

import math
N = int(input())
data = []
for _ in range(N):
    x, l = map(int, input().split())
    data.append([x+l, x-l])
data.sort()

ans = 0
tmp = -math.inf
for i in range(len(data)):
    # ひとつ前の右端と現在の区間の左端を比較
    if tmp <= data[i][1]:
        ans += 1
        tmp = data[i][0]

print(ans)
