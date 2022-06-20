N, Q = map(int, input().split())
A = list(map(int, input().split()))
shift = 0
for i in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:
        x, y = (x-1-shift)%N, (y-1-shift)%N
        A[x], A[y] = A[y], A[x]

    elif t == 2:
        shift += 1

    elif t == 3:
        print(A[(x-1-shift)%N])