# いもす法 : 要素の重複を効率よく数えるアルゴリズム
# 下記ビジュアルイメージ
# https://imoz.jp/algorithms/imos_method.html

N = int(input())
cnt = [[0] * 1001 for _ in range(1001)]
for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    cnt[lx][ly] += 1
    cnt[lx][ry] -= 1
    cnt[rx][ly] -= 1
    cnt[rx][ry] += 1

for i in range(1001):
    for j in range(1, 1001):
        cnt[i][j] += cnt[i][j-1]

for j in range(1001):
    for i in range(1, 1001):
        cnt[i][j] += cnt[i-1][j]

ans = [0] * (N+1)
for i in range(1001):
    for j in range(1001):
        ans[cnt[i][j]] += 1
for k in range(1, N+1):
    print(ans[k])
