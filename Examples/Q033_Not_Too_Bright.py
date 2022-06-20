H, W = map(int, input().split())

# コーナーケース
if H == 1 or W == 1:
    print(H*W)
else:
    ans = ((H+1)//2) * ((W+1)//2)
    print(ans)
