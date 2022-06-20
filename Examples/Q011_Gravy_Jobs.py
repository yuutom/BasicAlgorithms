N = int(input())
W = []
for _ in range(N):
    d, c, s = map(int, input().split())
    W.append([d, c, s])
# [d, c, s]のうち一番最初の要素 d でソートする
# ちなみにdictのソートは次のようにできる。sort(dict, key=lambda x: x['key名'])
W.sort(key=lambda x: x[0])

# dp[i][j] = 仕事iまで見ている状態で、合計day日作業している場合の報酬の最大値
dp = [[0] * 5002 for _ in range(N+1)]

for i in range(N):
    d, c, s = W[i]
    for day in range(1, 5001):
        # 仕事をする場合
        if c <= day <= d:
            dp[i+1][day] = max(dp[i][day], dp[i+1][day-1], dp[i][day-c]+s)
        else:
            dp[i+1][day] = max(dp[i][day], dp[i+1][day-1])

print(max(dp[N]))
