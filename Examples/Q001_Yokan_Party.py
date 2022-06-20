N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

# 長さM以上の、k+1個以上のピースに分割可能か否か
def solve(M: int):
  cnt = 0
  pre = 0
  for i in range(N):
    # 「左からi個目の切れ目までの長さ >= M」かつ「全体-左からi個目の切れ目までの長さ >= M」
    if (A[i] - pre >= M) & (L - A[i] >= M):
      cnt += 1
      pre = A[i]
  return cnt >= K

left = 0
right = L
while right - left > 1 :
    mid = (left+right)//2
    if solve(mid):
        left = mid
    else:
        right = mid

print(left)

print(ng)