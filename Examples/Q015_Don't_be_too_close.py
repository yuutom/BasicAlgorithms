# N 個のボールのうち、差が k 以上となるように　i 個のボールを選ぶ方法は
# N-(k-1)(i-1) C i 通りである
# nCk = n!/k!(n-k)!

class FactorialMod:
    def __init__(self, max_num, mod):
        """
        max_num : 作成するリストの最大数
        mod : 素数の mod
        inverse : 逆元
        factorial : 階乗
        factorial_inverse : 階乗の逆元
        """

        self.max_num = (max_num + 2)
        self.mod = mod
        self.inverse = [0] * self.max_num
        self.factorial = [0] * self.max_num
        self.factorial_inverse = [0] * self.max_num
        self.__calc_inverse()
        self.__calc_factorial()
        self.__calc_factorial_inverse()

    # ファルマーの小定理を用いて逆元を計算している
    # 割り算が掛け算に変換され、計算途中でmodを取ることが出来るようになっている
    # inverse[i] = ((i)^(-1) mod p)
    # inverse[2] = 500000004
    def __calc_inverse(self):
        self.inverse[1] = 1
        for i in range(2, self.max_num):
            self.inverse[i] = self.mod - ((self.mod // i) * self.inverse[self.mod % i] % self.mod)

    # factorial[5] = 5*4*3*2*1 = 120
    def __calc_factorial(self):
        self.factorial[0] = 1
        for i in range(1, self.max_num):
            self.factorial[i] = (self.factorial[i-1] * i) % self.mod

    # factorial_inverse[i] = ((i!)^(-1) mod p)
    def __calc_factorial_inverse(self):
        self.factorial_inverse[0] = 1
        for i in range(1, self.max_num):
            self.factorial_inverse[i] = (self.factorial_inverse[i-1] * self.inverse[i]) % self.mod

    # nCk を返す
    def combination_mod(self, n, k):
        if n < 0 or k < 0 or n > self.max_num or k > self.max_num or k > n:
            return 0
        return self.factorial[n] * self.factorial_inverse[k] % self.mod * self.factorial_inverse[n-k] % self.mod


def query(k):
    ret = 0
    for i in range(1, N//k + 2):
        s1 = N - (k-1)*(i-1)
        s2 = i
        ret += fac.combination_mod(s1, s2)
        ret %= mod
    return ret


N = int(input())
mod = 10 ** 9 + 7
fac = FactorialMod(10**5 + 5, mod)

for i in range(1, N+1):
    ans = query(i)
    print(ans)
