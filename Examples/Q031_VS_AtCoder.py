# https://qiita.com/masa0599/items/020b9ed3acb575ec89ac#grundy%E6%95%B0%E3%81%A7%E5%8B%9D%E6%95%97%E3%81%AE%E5%88%A4%E5%AE%9A
# https://qiita.com/masa0599/items/c85e3a5a1b80910f8e51

# 同じ盤面でどちらも同じ手を打てるゼロ和ゲームで、更に必ず有限手数で終了する時は、Grundy数を計算する。
# Grundy数G(P)G(P)とは
# ・負けが確定した状態PlostのときG(Plost)=0
# ・PPから1手で遷移できる状態がP′1,P′2,...,P′kだとすると G(P)=mex(G(P′1),G(P′2),...,G(P′k))
# ・ここでmex(Minimum excludant)は引数に含まれない最小の非負整数で、例えばmex(0,1,3)=2mex(0,1,3)=2となります。
# ・Grundy数が 0 の場合は後手必勝、 1 以上の場合は先手必勝

N = int(input())
W = map(int, input().split())
B = map(int, input().split())

# grundy[i][j] = 白石 i 個、青石 j 個の Grundy数
# w, b = 50, 50 からスタートすると、最大の b は 50+(50+1)*50//2=1325
grundy = [[-1]*1326 for _ in range(51)]
# w == 0 かつ b <= 1となると負け
grundy[0][0] = 0
grundy[0][1] = 0

# 白石の最大個数 : Wi 個
for w in range(51):
    # 青石の最大個数 :
    for b in range(1326):
        # 操作①を選んだ時のgrundy数の集合と操作②を選んだ時のgrundy数の集合の和を求める
        nex_grundy_set = set()
        if w >= 1:
            # 選択肢①を選べる時
            # 選んだ山に青石を w 個加え、白石を 1 個取り除く
            if b + w <= 1325:
                nex_grundy = grundy[w-1][b+w]
                nex_grundy_set.add(nex_grundy)
        if b >= 2:
            # 選択肢②を選べる時
            # 1 以上 b/2 以下の整数 k を選び、選んだ山から青石を k 個取り除く
            for k in range(1, b//2+1):
                nex_grundy = grundy[w][b-k]
                nex_grundy_set.add(nex_grundy)
        # 単純に0からリストの最大値まで見ていって、ない数があったらそれを返し、もし全部あった場合は最大値+1を返す
        # mex はリストの中の最小の非負整数
        for mex in range(1326):
            if mex not in nex_grundy_set:
                break
        grundy[w][b] = mex

ans = 0
# grundy[w][b] をすべて xor した値が 0 かどうかを判定
for w, b in zip(W, B):
    ans ^= grundy[w][b]

if ans == 0:
    print('Second')
else:
    print('First')
