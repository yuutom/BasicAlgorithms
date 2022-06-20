# 素因数分解
# 合成数 M は必ず 2 以上 √M 以下の整数で割り切れる
import math


# n を素因数分解
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(math.ceil(math.sqrt(n)))+1):
        if temp % i == 0:
            cnt = 0
            # 素因数 i が何個含まれているか
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    # n 自身が素数だった場合
    if temp != 1:
        arr.append([temp, 1])
    return arr


N = int(input())
d = factorization(N)
# 素因数の個数の合計
num = sum(i[1] for i in d)
if num == 1:
    print(0)
else:
    i = 0
    # 最小の操作回数は 2**x >= num を満たす最小の x となる
    while True:
        if num <= 2**i:
            break
        i += 1
    print(i)