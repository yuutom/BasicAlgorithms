from math import atan2, degrees
from bisect import bisect_left

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

ans = 0

# 中心の点を決め、その他の点との偏角を求める → リストに入れてソート
for i in range(N):
    xi, yi = A[i]
    D = []
    for j in range(N):
        if j != i:
            x, y = A[j]
            # atan2(y, x) = arctan(y / x)のラジアン
            # この角度は、極座標平面において原点から座標(x, y)へのベクトルがx軸の正の方向となす角度(偏角)を表す
            # 戻り値として、-piからpi（-180度から180度）を返す
            D.append(degrees(atan2(yi-y, xi-x)) % 360)
    D.sort()

    # 中心の点以外の各点毎に、その偏角に180°加えたものに近いものを探していく
    for k in range(N-1):
        # 二分探索 → index
        # idx = 偏角に180°加えたものに最も近いindex
        idx = bisect_left(D, (D[k]+180) % 360)
        # N-1の余りなのは、もし D[k]+180 がDのうち最大だった場合、idx = Dのリスト数 となり、
        # 下記の D[idx1] で IndexError となる
        idx1 = idx % (N-1)
        idx2 = (idx - 1) % (N-1)
        ans = max(ans, min(abs(D[idx1]-D[k]), 360 - abs(D[idx1]-D[k])))
        ans = max(ans, min(abs(D[idx2]-D[k]), 360 - abs(D[idx2]-D[k])))
print(ans)
