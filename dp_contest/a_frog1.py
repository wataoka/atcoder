N = int(input())
h = list(map(int, input().split()))

INF = 10**4 + 1
dp = [INF] * N
dp[0] = 0
dp[1] = abs(h[0] - h[1])

for i in range(N-2):
    dp[i+2] = min(dp[i+1]+abs(h[i+1]-h[i+2]), dp[i]+abs(h[i]-h[i+2]))

print(dp[-1])