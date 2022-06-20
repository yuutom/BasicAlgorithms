N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].append(b)
    G[b].append(a)

ans = 0
for i in range(N):
    count = 0
    for x in G[i]:
        if x < i:
            count += 1
    if count == 1:
        ans += 1
print(ans)
