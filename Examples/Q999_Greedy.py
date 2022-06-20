# 貪欲法, Greedy
# https://atcoder.jp/contests/abc091/tasks/arc092_a

N = int(input())
red = [list(map(int, input().split())) for _ in range(N)]
blue = [list(map(int, input().split())) for _ in range(N)]

# 赤い点が、青い点の左下にあればよい
# やみくもにペアにしていったら、それが最適かどうかわからない
# 青い点は左から考える
blue.sort(key=lambda x: x[0])
# 赤い点は上から考える
red.sort(key=lambda x: x[1], reverse=True)

ans = 0
for i in range(len(red)):
    for j in range(len(blue)):
        if red[i][0] < blue[j][0] and red[i][1] < blue[j][1]:
            ans += 1
            del blue[j]
            break
print(ans)
