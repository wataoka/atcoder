import math

n, k = map(int, input().split())
ans = []
for i in range(1, n+1):
    wins = 0
    score = i
    while True:
        if score >= k:
            break
        score *= 2
        wins += 1
    ans.append(pow(0.5, wins))
print(sum(ans)/len(ans))