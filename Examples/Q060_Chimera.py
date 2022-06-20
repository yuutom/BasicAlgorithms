# 最長増加部分列(LIS)

from bisect import *

N = int(input())
A = list(map(int, input().split()))

# 左側からの増加列
# dp[i] = 増加部分列の長さが i の部分列の内、部分列の最終要素の最も低い値
# 例えば、長さが 3 の次の増加部分列 = [1, 3, 5], [2, 3, 4] がある時 dp[3] = 4 となる
dp = [A[0]]
# 部分列の長さを記録
P = [0] * N
Q = [0] * N
P[0] = 1
Q[N-1] = 1
for i in range(1, N):
    # 一番大きいものより大きければ最後に追加
    if A[i] > dp[-1]:
        dp.append(A[i])
        P[i] = len(dp)
    # 上記以外の場合は昇順にその値を既存の値と入れ替える（単調性は崩れない）
    else:
        idx = bisect_left(dp, A[i])
        dp[idx] = A[i]
        P[i] = idx + 1

# 右側からの増加列
dp2 = [A[N-1]]
for i in range(N-2, -1, -1):
    # 一番大きいものより大きければ最後に追加
    if A[i] > dp2[-1]:
        dp2.append(A[i])
        Q[i] = len(dp2)
    else:
        idx = bisect_left(dp2, A[i])
        dp2[idx] = A[i]
        Q[i] = idx + 1

ans = 0
for i in range(N):
    if P[i] + Q[i] - 1 > ans:
        ans = P[i] + Q[i] - 1

print(ans)