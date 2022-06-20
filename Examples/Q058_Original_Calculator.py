N, K = map(int, input().split())


def f(x):
    return (x + sum(map(int, str(x)))) % 100000


done = [-1] * 100000
idx = 0
now = N
while True:
    # 同じ数が二回出現
    if done[now] != -1:
        # 周期 = 今の index - 前回の出現
        loop = idx - done[now]
        break
    done[now] = idx
    now = f(now)
    idx += 1

if K >= 100000:
    K = (K-100000)%loop + 100000

for _ in range(K):
    N = f(N)

print(N)

