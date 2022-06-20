# dfs, 深さ優先探索
# https://atcoder.jp/contests/atc001/tasks/dfs_a

import sys
sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if grid[i][j] == 's':
            sy, sx = i, j
        if grid[i][j] == 'g':
            gy, gx = i, j

visited = [[False]*W for _ in range(H)]
visited[sy][sx] = True


def dfs(x, y):
    visited[y][x] = True
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x+dx, y+dy
        if nx<0 or nx>=W or ny<0 or ny>=H:
            continue
        if grid[ny][nx]=='#':
            continue
        if not visited[ny][nx]:
            dfs(nx, ny)

dfs(sx, sy)
if visited[gy][gx]:
    print('Yes')
else:
    print('No')
