# dp
# https://atcoder.jp/contests/tdpc/tasks/tdpc_contest

N = int(input())
P = list(map(int, input().split()))

dp = [[False]*10001 for _ in range(N+1)]
dp[0][0] = True
for i in range(1, N+1):
    p = P[i-1]
    for j in range(10001):
        dp[i][j] = dp[i-1][j]
        if j-p >= 0:
            dp[i][j] = dp[i][j] or dp[i-1][j-p]
# sum() でリスト内の True の数を数える
print(sum(dp[N]))