N, K = map(int, input().split())
A = list(map(int, input().split()))

dict = {}
# 右端の index
head = 0
# 左端の index
tail = 0

ans = -1

# i : 添字, v : A の要素
for i, v in enumerate(A):
    head = i
    if v not in dict:
        # dict = {'v': 1} （key = v, value = 1）
        dict[v] = 1
    else:
        dict[v] += 1

    while len(dict) > K:
        tmp = A[tail]
        dict[tmp] -= 1
        if dict[tmp] == 0:
            del dict[tmp]
        tail += 1
    ans = max(ans, head-tail+1)

print(ans)