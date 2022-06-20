H, W = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(H)]
sum_i = []
sum_j = []

for x in range(H):
    sum_j.append(sum(matrix[x]))

for v in range(W):
    sum_i_temp = 0
    for w in range(H):
        sum_i_temp += matrix[w][v]
    sum_i.append(sum_i_temp)

for i in range(H):
    answer = []
    for j in range(W):
        answer.append(sum_i[j] + sum_j[i] - matrix[i][j])
    print(*answer)
