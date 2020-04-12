N, M = map(int, input().split())

num = [-1]*N
flag = False
for _ in range(M):
    s, c = map(int, input().split())
    if num[s-1] != -1 and num[s-1] != c:
        flag = True
    else:
        num[s-1] = c

# 無理な代入
if flag:
    print('-1')
    exit(0)

# 長さが1である時
if len(num) == 1:
    if num[0] == -1:
        print(0)
    else:
        print(num[0])
    exit(0)

# 先頭が-1である時
if num[0] == -1:
    num[0] = 1

# -1を0に変換
for i in range(N):
    if num[i] == -1:
        num[i] = 0


num = list(map(str, num))
print(''.join(num))