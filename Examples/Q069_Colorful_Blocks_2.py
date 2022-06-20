N, K = map(int, input().split())
mod = 10**9+7
if N == 1:
    print(K)
elif N == 2:
    print(K*(K-1)%mod)
else:
    if K <= 2:
        print(0)
    else:
        # a**b mod m は以下の繰返ニ乗法を使う(pow で実現)
        # pow の引数三つでべき乗の剰余を計算
        # pow(2, 4, 3) = 2**4%3 = 1
        print(K*(K-1)%mod * pow(K-2, N-2, mod) % mod)
