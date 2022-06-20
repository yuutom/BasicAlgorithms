# bit全探索

H, W = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(H)]

ans = 0
# for i in range(1, 2**H) と同じ
# 行の選び方（行数 H に対して、2**H 通りある）を生成
for bit in range(1, 1<<H):
    # bin(x) = x の二進数表示
    # bin(5) = 0b101
    tmp = bin(bit)[2:]
    if len(tmp) < H:
        tmp = "0"*(H-len(tmp)) + tmp
    # リスト[ 開始位置 : 終了位置 : step数 ]
    # tmp = [1, 2, 3] → tmp[::-1] = [3, 2, 1]
    tmp = tmp[::-1]

    # 一致する数字の個数を調べる dict の初期化
    dict = {}

    # bit が立っている行番号を check に入れる
    check = []
    for j in range(len(tmp)):
        if tmp[j] == '1':
            check.append(j)
    # bit が立っている行番号について、各列の数字が一致しているか見る
    for k in range(W):
        # bit が立っている行のそれぞれの列の数字を入れる dict
        dict2 = {}
        for ii, v in enumerate(check):
            # 今点検している列の数字の登場回数を見る
            if G[v][k] not in dict2:
                dict2[G[v][k]] = 1
            else:
                dict2[G[v][k]] += 1
            # 今点検している列の数字の登場回数が len(check) と同じ
            # = 今見てる行ではその列に登場する数字は全部同じ → dict に登場回数を加算
            if dict2[G[v][k]] == len(check):
                if G[v][k] not in dict:
                    dict[G[v][k]] = len(check)
                else:
                    dict[G[v][k]] += len(check)
    # dict2[G[v][k]] == len(check) が偽で、dict の中身がからの場合、dict.values() がエラーにならないための前処理
    if len(dict) == 0:
        tmp2 = 1
    else:
        tmp2 = max(dict.values())
    ans = max(ans, tmp2)
print(ans)