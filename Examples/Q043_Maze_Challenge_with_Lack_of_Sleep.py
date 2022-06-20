from collections import deque

H, W = map(int, input().split())
sy, sx = map(int, input().split())
ty, tx = map(int, input().split())
sy, sx, ty, tx = sy-1, sx-1, ty-1, tx-1
maze = [list(input()) for _ in range(H)]

# turn[pos][d] = 位置 pos に d の方向 ([U, R, D, L]) から入ってきたときの最小方向転換数
turn = [[10**6]*4 for _ in range(H*W)]
que = deque()
for d in range(4):
    # sy*W+sx はスタート位置の pos を表す
    # 例えば、H, W = 3, 3 の 9 マスの迷路に対し、スタート位置 sy = 2, sx = 2 （→ sy = 1, sx = 1）の時、
    # pos = 4 となり、実際に前から数えて４番目の座標であることがわかる
    turn[sy*W+sx][d] = 0
    que.append((sy*W+sx, d))

# URDL
move = ((-1, 0), (0, 1), (1, 0), (0, -1))
while que:
    yx, pre_d = que.popleft()
    # 上記の sy*W+sx の逆算で、 y, x = sy, sx を算出
    y, x = yx//W, yx%W
    for i, [dy, dx] in enumerate(move):
        ny, nx = y+dy, x+dx
        if 0 <= ny < H and 0 <= nx < W and maze[ny][nx] != '#':
            nyx = ny * W + nx
            # i : 進む方角
            # pre_d : 今向いている方角
            if i == pre_d:
                if turn[nyx][i] > turn[yx][i]:
                    turn[nyx][i] = turn[yx][i]
                    que.appendleft((ny*W+nx, i))
                    for dir2 in range(4):
                        if dir2 != i:
                            turn[nyx][dir2] = min(turn[nyx][dir2], turn[nyx][i] + 1)
            else:
                if turn[nyx][i] > turn[yx][pre_d] + 1:
                    turn[nyx][i] = turn[yx][pre_d] + 1
                    que.append((ny*W+nx, i))
                    for dir2 in range(4):
                        if dir2 != i:
                            turn[nyx][dir2] = min(turn[nyx][dir2], turn[nyx][i] + 1)

print(min(turn[ty*W+tx]))