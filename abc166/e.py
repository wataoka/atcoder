N = int(input())
A = list(map(int, input().split()))

min_A = min(A)
max_A = max(A)

score = [0 for i in range(10**8+2)]

ans = 0
for i in range(N):
    ans += score[A[i]]
    for j in range(1, N-i):
        if A[i]+j > max_A:
            break
        score[A[i]+j] += 1
    for j in range(1, N-i):
        if A[i]-j < min_A:
            break
        if A[i]-j <= 0:
            break
        score[A[i]-j] += 1

print(ans)