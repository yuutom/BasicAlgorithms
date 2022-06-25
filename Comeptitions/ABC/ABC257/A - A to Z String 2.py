N, X = map(int, input().split())
alphabet = list(map(chr, range(97, 123)))
S = ''
for x in alphabet:
    S = S + x*N
print(S[X-1].upper())