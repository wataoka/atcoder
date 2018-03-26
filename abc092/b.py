n = int(input())
d, x = map(int, input().split())
a = list(map(int, [input() for i in range(n)]))

ans = 0

for t in range(1, d+1):
    for ai in a:
        if ai == 1:
            ans += 1
        elif t == 1 or t%ai==1:
            ans += 1
print(ans+x)
