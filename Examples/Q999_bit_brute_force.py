# bit全探索
# https://atcoder.jp/contests/arc061/tasks/arc061_a

S = list(input())
num = len(S)-1

ans = 0
for bit in range(1<<num):
    pre = 0
    for i in range(num):
        # bit を i 回右にシフトして 1 と論理積を取る（最下位の桁が 1 であるかどうかチェックする）
        if (bit>>i) & 1:
            ans += int(''.join(S[pre:i+1]))
            pre = i+1
    ans += int(''.join(S[pre:]))
print(ans)


# https://atcoder.jp/contests/abc079/tasks/abc079_c
ABCD = list(map(int, input()))

for bit in range(1<<3):
    ans = ABCD[0]
    calc = []
    for i in range(3):
        if bit>>i & 1:
           ans += ABCD[i+1]
           calc.append('+')
        else:
            ans -= ABCD[i+1]
            calc.append('-')
    if ans == 7:
        print(f'{ABCD[0]}{calc[0]}{ABCD[1]}{calc[1]}{ABCD[2]}{calc[2]}{ABCD[3]}=7')
        exit()