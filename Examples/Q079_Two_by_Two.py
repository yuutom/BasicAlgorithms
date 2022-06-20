H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

for i in range(H):
    for j in range(W):
        B[i][j] -= A[i][j]

count = 0
for h in range(H-1):
    for w in range(W-1):
        d = -B[h][w]
        count += abs(d)
        B[h][w] += d
        B[h][w+1] += d
        B[h+1][w] += d
        B[h+1][w+1] += d

for h in range(H):
    for w in range(W):
        if not B[h][w] == 0:
            print('No')
            exit()
print('Yes')
print(count)