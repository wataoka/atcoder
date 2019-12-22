S = list(input())
MOD = 10**9 + 7
# dp[i][j]: 先頭i文字として考えられるもののうち, 13で割った余りがjであるものの個数
dp = [[0 for _ in range(13)] for _ in range(10**5+1)]

if __name__ == "__main__":

    for j in range(13):
        dp[0][j] = 1
    for i in range(1, len(S)):
        s = S[i]
        if s != '?':
            continue
