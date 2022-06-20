# エラトステネスの篩、素数判定

from math import *

n = int(input())

prime = [True] * (n+1)
prime[0] = False
prime[1] = False
# エラトステネスの篩
for p in range(2, int(sqrt(n+1))+1):
    if prime[p]:
        for i in range(p*p, n+1, p):
            prime[i] = False

prime_list = [i for i in range(n+1) if prime(i)]