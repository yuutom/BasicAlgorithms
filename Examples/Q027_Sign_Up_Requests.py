N = int(input())
# 登録済みの一覧を set で管理
regist = set()
# 日にちなので 1 ~ N+1 に直す
for i in range(1, N+1):
    S = input()
    # 模試登録していない名前なら
    if S not in regist:
        # 登録して
        regist.add(S)
        # 日にちを出力
        print(i)
