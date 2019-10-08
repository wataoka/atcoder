N, W = map(int, input().split())

# dp[i][j]: 荷物iまでにおける重さj以下の最大価値
dp = [[0]*(W+1) for i in range(N+1)]

for i in range(N):
    w, v = map(int, input().split())
    for j in range(W-w, -1, -1):
        if w[i] > j:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j], dp[i][j-w[i]]+v[i])

print(dp[-1][-1])