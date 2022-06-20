# ラングレス圧縮

N = int(input())
S = input()

ans = N*(N-1)//2

n = 1
for i in range(1, N):
    if S[i-1] == S[i]:
        n += 1
    else:
        ans -= n*(n-1)//2
        n = 1
if n > 1:
    ans -= n*(n-1)//2

print(ans)