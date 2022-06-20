N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

num_a = [0]*46
num_b = [0]*46
num_c = [0]*46

for i in range(N):
    num_a[A[i]%46] += 1
    num_b[B[i]%46] += 1
    num_c[C[i]%46] += 1

A = set([i%46 for i in A])
B = set([i%46 for i in B])
C = set([i%46 for i in C])

ans = 0
for i in A:
    for j in B:
        for k in C:
            if (i+j+k)%46 == 0:
                ans += num_a[i%46] * num_b[j%46] * num_c[k%46]

print(ans)