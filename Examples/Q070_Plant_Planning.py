N = int(input())
X, Y = [], []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()

ansx = 0
ansy = 0
for i in range(N):
    mid = int(N/2)
    ansx += abs(X[i]-X[mid])
    ansy += abs(Y[i]-Y[mid])

print(ansx+ansy)