a, b, k = map(int, input().split())
if (a, b) == (0, 0):
    print(0, 0)
    exit(0)
if a - k < 0:
    print(0, max(0, b - (k-a)))
else:
    print(a-k, b)