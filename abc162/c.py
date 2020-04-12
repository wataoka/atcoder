from math import gcd

def ngcd(arr):
    res = arr[0]
    for i in range(1, len(arr)):
        res = gcd(res, arr[i])
    return res

k = int(input())

dp = [[[-1 for _ in range(201)] for _ in range(201)] for _ in range(201)]

ans = 0
for i in range(1, k+1):
    for j in range(1, k+1):
        for l in range(1, k+1):
            if dp[i][j][l] == -1:
                tmp = ngcd([i, j, l])
                dp[i][j][l] = tmp
                dp[i][l][j] = tmp
                dp[j][i][l] = tmp
                dp[j][l][i] = tmp
                dp[l][i][j] = tmp
                dp[l][j][i] = tmp
            ans += dp[i][j][l]

print(ans)