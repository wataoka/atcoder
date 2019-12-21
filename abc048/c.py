N, x = map(int, input().split())
a = [0]+list(map(int, input().split()))

cnt = 0
for i in range(1, N+1):
    if i == 1:
        if a[i]>x:
            cnt += a[i]-x
            a[i] -= a[i]-x
        continue
    if a[i-1]+a[i]>x:
        cnt += a[i]+a[i-1]-x
        a[i] -= a[i]+a[i-1]-x
print(cnt)