n, m = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) <= n:
    print(n - sum(A))
else:
    print(-1)