# 個数制限なしナップサックdp
#https://atcoder.jp/contests/abc153/tasks/abc153_e

H, N = map(int, input().split())
# A: 魔法の威力  B: 消費MP
A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

# dp[i][j] := i番目の魔法まで使い終わって、残りの体力がjであるときの、消費魔力の最小値
dp = [[float('inf')]*(H+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(H+1):
        if j <= A[i]:
            dp[i+1][j] = min(dp[i][j], B[i])
        elif j>A[i]:
            dp[i+1][j] = min(dp[i][j], dp[i+1][j], dp[i+1][j-A[i]]+B[i])

print(dp[N][H])
