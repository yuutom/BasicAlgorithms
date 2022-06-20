ans = 10000
N = int(input())
A = list(map(int, input().split()))
A.sort()

for i in range(10000):
    for j in range(10000-i):
        temp = N - A[2]*i - A[1]*j
        if temp >= 0 and temp % A[0] == 0:
            k = temp // A[0]
            ans = min(ans, i + j + k)

print(ans)
