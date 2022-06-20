# 転倒数

N = int(input())
L, R = [], []
for _ in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

ans = 0
for i in range(N):
    for j in range(i+1, N):
        for l in range(L[i], R[i]+1):
            # 転倒数としてカウント
            if R[j] < l:
                # j 番目の要素は L[j](最小) から R[j](最大) のどれか
                # R[j] < l であれば j 番目の要素は全て l より小さい → 全部が転倒数としてカウント出来る
                inv = R[j] - L[j] + 1
            else:
                # 上記でない場合は、 l に対して l より大きい分だけ転倒数としてカウント
                # L[j] > l であれば転倒数はない
                inv = max(0, l-L[j])

            dnmnt = (R[i]-L[i]+1)*(R[j]-L[j]+1)
            # 期待値の線形性
            ans += inv/dnmnt

print(ans)
