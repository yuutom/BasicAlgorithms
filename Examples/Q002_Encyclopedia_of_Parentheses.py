import itertools

# 括弧列が正しいかどうかの必要十分条件は以下
# ・'('と')'の数が等しい
# ・すべてのi (1 <= i <= N)に対して左からi番目までの時点で'('の数が')'よりも多い

def check_pair(i):
    if i[0] != '(':
        return False
    right = 0
    left = 0
    for x in i:
        if x == '(':
            left += 1
        else:
            right += 1
        if left < right:
            return False
    return True

N = int(input())
P = itertools.product('()', repeat = N)
for i in P:
    if check_pair(i) and i.count('(') == i.count(')'):
        print(*i, sep='')
