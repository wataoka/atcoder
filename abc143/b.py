n = int(input())
d = list(map(int, input().split()))

res = 0
for i in range(n):
    for j in range(i, n):
        if j!=i:
            res += d[i]*d[j]

print(res)