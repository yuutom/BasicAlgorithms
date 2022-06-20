# DP

N, L = map(int, input().split())
mod = 10**9 + 7
# dp[i] = i 段目まで到着する通り数
dp = [0] * (N+1)
dp[0] = 1

for i in range(1, N+1):
    if 0 <= i - L:
        dp[i] += dp[i-1] + dp[i-L]
        dp[i] %= mod
    else:
        dp[i] += dp[i-1]
        dp[i] %= mod

print(dp[N])