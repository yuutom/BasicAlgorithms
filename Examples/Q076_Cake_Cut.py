# 尺取り法
# https://qiita.com/drken/items/ecd1a472d3a0e7db8dce

N = int(input())
A = list(map(int, input().split()))
size = sum(A)//10

if size == 0:
    print('No')
    exit()

l, r = 0, 0
sum = 0
while r < 2*N:
    if sum + A[r%N] <= size:
        sum += A[r%N]
        r += 1
        if sum == size:
            print('Yes')
            exit()
    elif l == r:
        l, r = l+1, r+1
    else:
        sum -= A[l%N]
        l += 1
print('No')


# N = int(input())
# A = list(map(int, input().split()))
# size = sum(A)//10
#
# if size == 0:
#     print('No')
#     exit()
#
# check_size = 0
# left, right = 0, 0
# # 尺取り法
# # 2*N としているのは、円環をリストに入れているから。
# # 例えば、A[N]+A[1]+A[2]… のようなケースを検証するため
# while right < 2*N:
#     check_size += A[right%N]
#     right += 1
#     while size < check_size:
#         check_size -= A[left%N]
#         left += 1
#
#     if size == check_size:
#         print('Yes')
#         exit()
# print('No')
