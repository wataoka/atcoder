N = int(input())
a = list(map(int, input().split()))

i = 1
ans = 0
for ai in a:
    if ai == i:
        i += 1
    else:
        ans += 1
if ans == N:
    print(-1)
else:
    print(ans)