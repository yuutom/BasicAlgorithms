from math import *
T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

for _ in range(Q):
    ans = 0
    # theta = Ei 分後の観覧車の回転した角度 = 360° * Ei/T
    theta = 2 * pi * int(input()) / T
    y = -L/2 * sin(theta)
    z = L/2 - L/2 * cos(theta)
    # d = 二辺の長さが X, Y - y の三角形の斜辺の長さ（三平方の定理）
    d = hypot(X, Y - y)
    # 高さ z, 距離 d のなす三角形の角度
    ans = degrees(atan2(z, d))
    print(ans)