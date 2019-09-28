n, k = map(int, input().split())
h = list(map(int, input().split()))

res = 0
for h_i in h:
    if h_i >= k:
        res += 1

print(res)