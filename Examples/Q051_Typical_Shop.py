# 半分全列挙, bit全探索

from bisect import *

N, K, P = map(int, input().split())
A = list(map(int, input().split()))

A1 = A[:N//2]
A2 = A[N//2:]
la1 = len(A1)
la2 = len(A2)

ans1 = [[] for _ in range(K+1)]
# 1<<la1 : 1 を la1 分左ビットシフト
# la1 = 3 の場合、 1(2) → 1000(2) → 8(10)
for bit in range(1<<la1):
    cost = 0
    cnt = 0
    # bit全探索
    for i in range(la1):
        # 1 を i ビットだけ左にずらして bit と AND演算
        # 演算結果が 0 以外で if 以下実行
        if bit & 1 << i:
            cnt += 1
            cost += A1[i]
    if cnt <= K and cost <= P:
        ans1[cnt].append(cost)

ans2 = [[] for _ in range(K+1)]
for bit in range(1<<la2):
    cost = 0
    cnt = 0
    for i in range(la2):
        if bit & 1 << i:
            cnt += 1
            cost += A2[i]
    if cnt <= K and cost <= P:
        ans2[cnt].append(cost)

for i in range(K+1):
    ans1[i].sort()
    ans2[i].sort()

ans = 0
# 二分探索
for i in range(K+1):
    i2 = K-i
    for j in range(len(ans1[i])):
        # 以下にしたいので right
        # bisect_right(ソート済みの配列, 挿入したい値) = 挿入する index を返す
        ans += bisect_right(ans2[i2], P-ans1[i][j])

print(ans)
