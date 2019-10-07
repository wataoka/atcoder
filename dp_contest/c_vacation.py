N = int(input())
abc = []
for i in range(N):
    abc.append(list(map(int, input().split())))

# dp[i][j] i日の時に行動jを起こす状況における最大幸福
dp = [[0]*3 for i in range(N)]
dp[0][0] = abc[0][0]
dp[0][1] = abc[0][1]
dp[0][2] = abc[0][2]

for i in range(N-1):
    for j in range(3):
        actions = list(set([0, 1, 2]) - set([j]))
        dp[i+1][j] = max(list(map(lambda x: abc[i+1][j]+dp[i][x], actions)))

print(max(dp[-1]))