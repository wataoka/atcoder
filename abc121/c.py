n, m = map(int, input().split())
AB = []
for i in range(n):
    AB.append(list(map(int, input().split())))
AB = sorted(AB, key=lambda x:x[0])
ans = 0
cnt = 0 
for a, b in AB:
    pre_cnt = cnt
    cnt += b
    if cnt >= m:
        ans += a*(m-pre_cnt)
        break
    else:
        ans += a*b
print(ans)