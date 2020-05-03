from collections import Counter

N = int(input())
A = list(map(int, input().split()))
min_A = min(A)
max_A = max(A)

ans = 0
score = [{} for i in range(N+1)]
for i in range(N):
    if A[i] in score[i].keys():
        ans += score[i][A[i]]
    for j in range(1, N-i+1):
        if A[i]+j > max_A:
            break
        if A[i]+j in score[i+j].keys():
            score[i+j][A[i]+j] += 1
        else:
            score[i+j][A[i]+j] = 1
    for j in range(1, N-i+1):
        if A[i]-j < min_A:
            break
        if A[i]-j in score[i+j].keys():
            score[i+j][A[i]-j] += 1
        else:
            score[i+j][A[i]-j] = 1

print(ans)