N, K = map(int, input().split())
AB = []
for i in range(N):
    A, B = map(int, input().split())
    AB.append(B)
    AB.append(A-B)
AB.sort()

ans = 0
for _ in range(K):
    ans += AB.pop()

print(ans)