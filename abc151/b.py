n, k, m = map(int, input().split())
a = list(map(int, input().split()))

an = m*n - sum(a)

if an < 0:
    print(0)
elif an > k:
    print(-1)
else:
    print(an)