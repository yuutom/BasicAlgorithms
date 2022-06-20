def get_all_deviders(target):
    i = 1
    res = []
    while i ** 2 <= target:
        if target % i == 0:
            res.append(i)
            # i = 1 の時、res に 12 を追加
            # i = 2 の時、res に 6 を追加
            if not target // i == i:
                res.append(target//i)
        i += 1
    res.sort()
    # target = 12 の場合、res = [1, 2, 3, 4, 6, 12]
    return res


K = int(input())
count = 0
for smallest in get_all_deviders(K):
    if K//smallest < smallest:
        break
    rest = K // smallest
    for middle in get_all_deviders(rest):
        if middle < smallest:
            continue
        largest = rest//middle
        if largest < middle:
            break
        if largest >= smallest:
            count += 1

print(count)