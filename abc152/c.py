N = int(input())
P = list(map(int, input().split()))

ans = 1
minP = P[0]
for i in range(1, N):
    if minP >= P[i]:
        minP = P[i]
        ans += 1
print(ans)