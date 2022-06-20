N, k = input().split()
K = int(k)


# 10進数からN進数へ
def base_10_to_n(x, n):
    dumy = x
    ans = ''
    while dumy>0:
        ans = str(dumy%n) + ans
        dumy //= n
    return ans


if N == '0':
    print(0)
    exit()

for i in range(K):
    eightToTen = 0
    for j in range(len(N)):
        eightToTen += int(N[-j-1]) * (8**j)
    tenToNine = base_10_to_n(eightToTen, 9)
    N = tenToNine.replace('8', '5')

print(N)