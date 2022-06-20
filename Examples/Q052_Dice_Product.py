N = int(input())
mod = 10**9 + 7
ans = 1
for i in range(N):
    A = list(map(int, input().split()))
    sum_A = sum(A)
    ans *= sum_A

print(ans%mod)
