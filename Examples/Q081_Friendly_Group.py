# 二次元累積和

N, K = map(int, input().split())
m = 5000

g = [[0]*(m+1) for _ in range(m+1)]
# データを二次元にプロット
for _ in range(N):
    a, b = map(int, input().split())
    g[a][b] += 1

# 行→列の累積和をとる
# g[i][j] = 身長 i 以下かつ体重 j 以下の生徒の人数
for i in range(m+1):
    for j in range(m):
        g[i][j+1] += g[i][j]
for i in range(m):
    for j in range(m+1):
        g[i+1][j] += g[i][j]

ans = 0
for i in range(1, m+1):
    for j in range(1, m+1):
        ly, lx = max(0, i-K-1), max(0, j-K-1)
        ry, rx = i, j
        ans = max(ans, g[ry][rx]-g[ry][lx]-g[ly][rx]+g[ly][lx])
print(ans)
