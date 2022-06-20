N = int(input())
A = list(map(int, input().split()))
Q = int(input())

A.sort()


def binary_search(b):
    left = 0
    right = N-1
    while right - left > 1:
        mid = (left+right)//2
        if b < A[mid]:
            right = mid
        else:
            left = mid

    return min(abs(b-A[left]), abs(b-A[right]))


for _ in range(Q):
    print(binary_search(int(input())))
