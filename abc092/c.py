n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)
a.append(0)

ans = 0
for i in range(len(a)-1):
    ans += abs(a[i] - a[i+1])
tmp = ans

for i in range(1, len(a)-1):
    ans = tmp
    if (a[i]-a[i+1])*(a[i]-a[i-i]) < 0:
        print(ans)
    else:
        ans -= abs(a[i-1]-a[i]) + abs(a[i+1] - a[i])
        ans += abs(a[i+1] - a[i-1])
        print(ans)

