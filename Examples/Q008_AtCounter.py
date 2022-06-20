mod = 10 ** 9 + 7
N = int(input())
S = input()

str = ['a','t','c','o','d','e','r']
# 8 は str の要素数 +1
# dp[i][j] = 入力文字列 S の位置 i, 'atcoder' の j 文字目まで選んだ時の通り数
dp = [[0] * 8 for _ in range(N+1)]
dp[0][0] = 1

for i in range(N+1):
  dp[i][0] = 1

for i in range(N):
  for j in range(7):
    if S[i] == str[j]:
      dp[i+1][j+1] = dp[i][j] + dp[i][j+1]
    else:
      dp[i+1][j+1] = dp[i][j+1]

# for x in dp:
  # print(*x)
print(dp[N][7]%mod)