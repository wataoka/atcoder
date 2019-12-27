from math import floor

N, M, K = map(int, input().split())
A = []
for _ in range(N+1):
    A.append(int(input()))

# dp[i][j]: i分目まで終了してj回売買を済ませた場合の資金の最大値
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
dp[0][0] = K

ans = 0
for i in range(1, N+1):
    for j in range(0, min(M+1, i+1)):
        dp[i][j] = max(dp[i][j], dp[i-1][j])
        if j>0:
            for k in range(i):
                dp[i][j] = max(dp[i][j], floor(dp[k][j-1]/A[k])*A[i] + dp[k][j-1]%A[k])
        ans = max(ans, dp[i][j])

for i in dp:
    print(i)