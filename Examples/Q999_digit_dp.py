# 桁DP
# https://atcoder.jp/contests/tdpc/tasks/tdpc_number
# https://qiita.com/pinokions009/items/1e98252718eeeeb5c9ab

D = int(input())
N = int(input())
N_separated = list(map(int, str(N)))
mod = 1000000007
digit = len(str(N))

# dp[i][j][k] = i, j, k が下記の条件の時の個数
# i:上からi桁目まで参照している
# j:N未満であることが確定しているかどうか(j=1で確定、j=0で確定していない)
# k:各桁の和をDで割った余り
dp = [[[0] * D for _ in range(2)] for _ in range(digit + 1)]
dp[0][0][0] = 1
for i in range(digit):
    for k in range(D):
        for num in range(10):
            # 未満フラグが 1 (N 未満であることが確定)のため、0~9 好きな数字を入れてよい
            # Nより小さかったので次も小さくなる場合, j=1のまま
            # N = 1234 の場合で、現在 i = 1 を見ている場合、例えば N = 112* となる場合など(上からi 桁目が 1, i+1 桁目が 2)
            dp[i + 1][1][(k + num) % D] += dp[i][1][k]
            dp[i + 1][1][(k + num) % D] %= mod

            # Nと同じだったがNより小さくなる場合. jは0が1になる
            # N = 1234 の場合で、現在 i = 1 を見ている場合、例えば N = 122* となる場合など(上からi 桁目が 2, i+1 桁目が 2)
            if num < N_separated[i]:
                dp[i+1][1][(k+num)%D] += dp[i][0][k]
                dp[i+1][1][(k+num)%D] %= mod

            # Nと同じだったがまたNと同じになる場合. j=0のまま
            # N = 1234 の場合で、現在 i = 1 を見ている場合、例えば N = 123* となる場合など(上からi 桁目が 2, i+1 桁目が 3)
            if num == N_separated[i]:
                dp[i+1][0][(k+num)%D] += dp[i][0][k]
                dp[i+1][0][(k+num)%D] %= mod

# dp[Digit][0][0]は0をカウントしてしまっているので1を引く
print((dp[digit][0][0]+dp[digit][1][0]-1)%mod)
