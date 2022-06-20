# ワーシャルフロイド法, 二分探索

N, P, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]


def warshall_floyd(mid):
    # c[i][j] = i から j までの距離
    c = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] == -1:
                c[i][j] = mid
            else:
                c[i][j] = A[i][j]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                c[i][j] = min(c[i][j], c[i][k]+c[k][j])

    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if c[i][j] <= P:
                cnt += 1

    return cnt


LR = []
for _ in range(2):
    L = 0
    R = 10**9 + 1
    while R-L > 1:
        mid = (R+L)//2
        cnt = warshall_floyd(mid)
        if cnt >= K+1:
            L = mid
        else:
            R = mid
    LR.append(L)
    K -= 1

if LR[0] == 10**9:
    print(0)
elif LR[1] == 10**9:
    print('Infinity')
else:
    print(LR[1]-LR[0])
