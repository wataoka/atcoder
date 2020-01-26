N, M, C = map(int, input().split())
B = list(map(int, input().split()))
ans = 0
for i in range(N):
    A = list(map(int, input().split()))
    res = 0
    for j in range(M):
        res += A[j]*B[j]
    res += C
    if res > 0:
        ans += 1
print(ans)