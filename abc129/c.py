N, M = map(int, input().split())

mod = 10**9+7
dp = [0]*(N+1)
dp[0] = 1
for i in range(1, M+1):
    a = int(input())
    dp[a] = -1
for i in range(0, N-1):
    if dp[i] == -1:
        continue
    if dp[i+1] != -1:
        dp[i+1] += dp[i]%mod
        dp[i+1] %= mod
    if dp[i+2] != -1:
        dp[i+2] += dp[i]%mod
        dp[i+2] %= mod
if dp[-2] != -1:
    dp[-1] += dp[-2]%mod
    dp[-1] %= mod
print(dp[-1])