H, N = map(int, input().split())
A = list(map(int, input().split()))

sumA = sum(A)
if sumA>=H:
    print('Yes')
else:
    print('No')