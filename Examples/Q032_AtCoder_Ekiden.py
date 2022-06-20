import itertools

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
XY = [list(map(int, input().split())) for _ in range(M)]

# 選手 x, y の仲が悪いかを格納する bool 型配列
# 選手 x, y の仲が悪い → a[x-i][y-1] = True
a =[[False] * N for _ in range(N)]
for xy in XY:
    x, y = xy
    a[x-1][y-1] = True
    a[y-1][x-1] = True

num = 10001
for p in itertools.permutations(range(N)):
    time = 0
    flag = True
    for i in range(N-1):
        if a[p[i]][p[i+1]]:
            flag = False
            break
    if flag:
        for j in range(N):
            time += A[p[j]][j]
        num = min(num, time)

print(num if num != 10001 else -1)