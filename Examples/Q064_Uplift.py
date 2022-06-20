N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = []
S = 0
ans = []

for i in range(N-1):
    B.append(A[i+1] - A[i])
    S += abs(B[i])

for i in range(Q):
    l, r, v = map(int, input().split())
    l, r = l-1, r-1
    if l-1 >= 0:
        B[l-1] += v
        S += abs(B[l-1]+v) - abs(B[l-1])
    if r < N-1:
        B[r] -= v
        S += abs(B[r]-v) - abs(B[r])
    ans.append(S)

print(*ans, sep='\n')
