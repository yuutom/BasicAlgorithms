N = int(input())
alist = [0]
blist = [0]

for i in range(N):
    C, P = map(int, input().split())
    if C == 1:
        alist.append(alist[i] + P)
        blist.append(blist[i])
    else:
        alist.append(alist[i])
        blist.append(blist[i] + P)

Q = int(input())
for j in range(Q):
    res_L = 0
    res_R = 0
    L, R = map(int, input().split())
    res_L = alist[R] - alist[L-1]
    res_R = blist[R] - blist[L-1]
    print(res_L, res_R)
    
