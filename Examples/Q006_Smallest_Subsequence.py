# 大きさKの部分文字列のうち最も辞書順が小さいものを選ぶ。

# 辞書順最小は前から貪欲に求めていくと良いらしい。aがあればaを、なければbを取るのが望ましい。
# 最小のものが複数ある場合は最も左にあるものを取れば良い

# ただし、取れる文字については制限がある。
# 今までとってきた文字数をi字として少なくともk-i字は右に残っていないと文字を選ぶことができなくなる。

# k回探すのは面倒なので、最初にどの文字がどの位置にあるかを記録しておく。
# pythonについてはlen(S)の計算量はO(1)となる。なぜなら、あらかじめ持っている情報だから。


# 前処理として以下のリストを計算しておく
# res[i][c] := i 文字目以降で最初に文字 c が登場する index
# 存在しないときは N を返す
def calc_next(s):
    n = len(s)
    res = [[n] * 26 for _ in range(n+1)]  # [[n,n,…, n], [n,n,…, n], …, [n,n,…, n]]
    for i in range(n-1, -1, -1):  # i = n-1, n-2, … , 1, 0
        # i + 1文字目をi文字目にコピー
        # 後ろから累積的に処理する必要がある
        # 例えば、文字列「abbba」を考える
        # 前から処理した場合、1文字目以降で最初に文字 a が登場するindexが、4文字目以降で最初に登場するindexに反映されてしまう
        for j in range(26):
            res[i][j] = res[i+1][j]

        # i文字目の情報を反映
        res[i][ord(s[i]) - ord('a')] = i

    return res


# 入力
N, K = map(int, input().split())
S = input()

# 前処理
res = ''
nex = calc_next(S)

# 貪欲法
j = -1
for i in range(K):
    for ordc in range(26):
        k = nex[j+1][ordc]
        if N - k >= K - i:
            res += chr(ord('a')+ordc)
            j = k
            break

print(res)
