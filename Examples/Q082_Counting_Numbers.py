MOD = 10**9 + 7
L, R = map(int, input().split())

ans = 0
# i = 桁数
# 例えば、L = 3, R = 15 の場合、 ans = (3~9まで個数)*1 + (10~15までの値)*2
for i in range(19):
    al = max(L, 10**i)
    ar = min(R, 10**(i+1)-1)
    # L = 88, R = 105 で、i = 0 の場合など
    if ar < al:
        continue
    ans += (ar*(ar+1)//2 - al*(al-1)//2) * (i+1)
    ans %= MOD

print(ans)