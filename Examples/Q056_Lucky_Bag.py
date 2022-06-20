# 復元DP

N, S = map(int, input().split())
A, B = [], []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

# dp[i][j] = i 日目までの総和が j
dp = [[False] * (S+1) for _ in range(N+1)]
dp[0][0] = True

for i in range(N):
    for j in range(S+1):
        # i 日目までの総和が j が可能でなければ(dp[i][j] = False)以下スキップ
        if not dp[i][j]:
            # 以下全てをスキップして for j in range(S+1) に戻る
            continue
        if j + A[i] <= S:
            dp[i+1][j+A[i]] = True
        if j + B[i] <= S:
            dp[i+1][j+B[i]] = True

if not dp[N][S]:
    print('impossible')
    exit()

# 復元
ans = []
now = S
# 後ろから復元していく
for i in range(N, 0, -1):
    if now >= A[i-1] and dp[i-1][now-A[i-1]]:
        ans.append('A')
        now -= A[i-1]
    else:
        ans.append('B')
        now -= B[i-1]

# 配列のスライス
# ans[0:10:2] → ans を 0 から 10 まで 2 飛ばしで取得
# ans[::-1] → ans の全要素を逆順から取得
# join関数
# test = ['ab', 'c', 'de'] → ','.join(test) = ab,c,de
# test = ['ab', 'c', 'de'] → ''.join(test) = abcde
print(''.join(ans[::-1]))
