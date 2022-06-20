import math

A, B = map(int, input().split())
ans = (A*B) // math.gcd(A, B)

if ans <= 10**18:
    print(ans)
else:
    print('Large')
