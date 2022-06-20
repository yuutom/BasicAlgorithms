N, K = map(int, input().split())
# c[i] = i の素因数の種類数（c[15] = 2 (∵ 15 = 3 * 5)）
c = [0] * (N+1)

# エラトステネスの篩
# c[2], c[4], c[6], c[8], ・・・ に 1 を加算
# c[3], c[6], c[9], c[12], ・・・ に 1 を加算
# c[5], c[10], c[15], c[20], ・・・ に 1 を加算
# 上記を最後まで繰り返す
for i in range(2, N+1):
    if c[i] != 0:
        continue
    for j in range(i, N+1, i):
        c[j] += 1

ans = 0
for i in c:
    # i = 素因数の種類の数
    if i >= K:
        ans += 1

print(ans)
