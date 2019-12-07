N, T = map(int, input().split())
t = list(map(int, input().split()))

res = 0
pre_t = 0
for i in range(N):
    cur_t = t[i]

    if i==0:
        res+=T
    elif cur_t - pre_t >= T:
        res += T
    else:
        res += cur_t - pre_t

    pre_t = cur_t

print(res)