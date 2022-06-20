# 問題
# https://atcoder.jp/contests/tdpc/tasks/tdpc_dice
# 解説
# https://linearml.hatenablog.com/entry/competitive-programming/d-dice

N, D = map(int, input().split())

two = 0
three = 0
five = 0
while D%2 == 0:
    two += 1
    D //= 2
while D%3 == 0:
    three += 1
    D //= 3
while D%5 == 0:
    five += 1
    D //= 5
if D != 1:
    print(0)
    exit()
# dp[N][x][y][z] := N 回サイコロを振った時，2の素因数が x 個，3 の素因数が y 個，5 の素因数が z 個となる確率
dp = [[[[0]*(five+1) for _ in range(three+1)] for _ in range(two+1)] for _ in range(N+1)]
dp[0][0][0][0] = 1
for n in range(N):
    for i in range(two+1):
        for j in range(three+1):
            for k in range(five+1):
                p = dp[n][i][j][k]/6
                if p == 0:
                    continue
                dp[n+1][i][j][k] += p
                dp[n+1][min(i+1, two)][j][k] += p
                dp[n+1][i][min(j+1, three)][k] += p
                dp[n+1][min(i+2, two)][j][k] += p
                dp[n+1][i][j][min(k+1, five)] += p
                dp[n+1][min(i+1, two)][min(j+1, three)][k] += p
print(dp[N][two][three][five])

