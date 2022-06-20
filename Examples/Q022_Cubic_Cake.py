import math

a, b, c = map(int, input().split())

g = math.gcd(a, b)
g = math.gcd(g, c)

ans = (a//g - 1) + (b//g - 1) + (c//g - 1)
print(ans)