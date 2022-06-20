# 区間DP

N = int(input())
A = list(map(int, input().split()))
# dp[l][r] = l, l+1, …, r までの人が抜けるのに必要な最小コスト
dp = [[10**18] * (2*N) for _ in range(2*N)]

for i in range(2*N-1):
    dp[i][i+1] = abs(A[i] - A[i+1])

# width = 幅 (幅は 2 * width )
# 右端(r) と 左端(l) の間にある要素数を表す
for width in range(2, N+1):
    for l in range(2*N - 2*width + 1):
        r = l + 2*width - 1
        # パターン① : 最後に人 l, r が抜けるパターン
        now = dp[l+1][r-1] + abs(A[l]-A[r])
        for mid in range(1, width):
            # パターン② : 区間 [l, k] と区間 [k+1, l] に分けるパターン
            # パターン①とパターン②の小さいほうを登録
            now = min(now, dp[l][l+mid*2-1]+dp[l+mid*2][r])
        dp[l][r] = now

print(dp[0][-1])