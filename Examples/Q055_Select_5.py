# 全探索

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for i in range(N):
    for j in range(i):
        for k in range(j):
            for l in range(k):
                for m in range(l):
                    if A[i]%P*A[j]%P*A[k]%P*A[l]%P*A[m]%P == Q:
                        cnt += 1

print(cnt)