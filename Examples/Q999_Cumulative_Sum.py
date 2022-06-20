# 累積和
# https://atcoder.jp/contests/abc233/tasks/abc233_d
# https://qiita.com/sano192/items/e54a9f9b994781709881

from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

A_cum = [0]*(N+1)
for i in range(N):
    A_cum[i+1] = A_cum[i] + A[i]

X = defaultdict(int)
ans = 0
