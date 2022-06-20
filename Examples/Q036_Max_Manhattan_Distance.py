# N, Q = map(int, input().split())
# P = [list(map(int, input().split())) for _ in range(N)]
#
# for _ in range(Q):
#     dist = []
#     q = int(input())
#     q -= 1
#     for i in range(N):
#         d = 0
#         d = abs(P[q][0] - P[i][0]) + abs(P[q][1] - P[i][1])
#         dist.append(q)
#     print(max(dist))
#

# 上記は計算量 O(n^2) となり TLE
# マンハッタン距離は、 45° 回転させることで、計算量を O(n) に出来る
N, Q = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]
Query = [int(input()) for _ in range(Q)]

rotate = []
rotateX = []
rotateY = []

for i in range(N):
    x = P[i][0]
    y = P[i][1]
    rotateX.append(x+y)
    rotateY.append(x-y)
    rotate.append([x+y, x-y])

rotateX.sort()
rotateY.sort()

for q in Query:
    ans = max(abs(rotate[q-1][0] - rotateX[0]), abs(rotate[q-1][0] - rotateX[-1]),
        abs(rotate[q-1][1] - rotateY[0]), abs(rotate[q-1][1] - rotateY[-1]))
    print(ans)
