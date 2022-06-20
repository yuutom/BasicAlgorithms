# 木DP

import sys
sys.setrecursionlimit(10 ** 9)

N = int(input())
C = input().split()
G = [[] for _ in range(N)]
mod = 10 ** 9 + 7
dp = [[0] * 3 for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)


# dp[pos][state] = 頂点 pos の部分木を考えた時、state の状態の物は何通りか(「既に切られた連結成分が'a', 'b' 両方含む」を満たす)
# state → 0 : 'a'しかない/1 : 'b'しかない/2 : 'a', 'b' 両方ある
def dfs(pos, par):
    if C[pos] == 'a':
        state = 0
    else:
        state = 1
    dp[pos][state] = 1
    dp[pos][2] = 1
    for to in G[pos]:
        # 親の方に戻ろうとしている場合
        if par == to:
            # for 文の最初からやり直し
            continue
        dfs(to, pos)
        dp[pos][state] *= (dp[to][state] + dp[to][2])
        dp[pos][2] *= (dp[to][0] + dp[to][1] + 2 * dp[to][2])
    dp[pos][2] -= dp[pos][state]
    dp[pos][2] %= mod


dfs(0, -1)
print(dp[0][2])
