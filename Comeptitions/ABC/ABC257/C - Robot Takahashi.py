from bisect import *
N = int(input())
S = input()
W = list(map(int, input().split()))
ans = 0
adults = []
children = []
for i in range(N):
    if S[i] == '1':
        adults.append(W[i])
    else:
        children.append(W[i])
adults.sort()
children.sort()
a_count = len(adults)
c_count = len(children)
if a_count == 0 or c_count == 0:
    print(N)
    exit()
for a in adults:
    index1 = a_count - bisect_left(adults, a)
    index2 = bisect_left(children, a)
    ans = max(ans, index1+index2)
for c in children:
    index1 = a_count - bisect_left(adults, c)
    index2 = bisect_left(children, c)
    ans = max(ans, index1+index2)
print(ans)