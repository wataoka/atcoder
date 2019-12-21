N = int(input())
A = [0]+list(map(int, input().split()))

S = sum(A)
S_odd = 0
for i in range(1, N+1):
    if i==N or i%2==0:
        continue
    S_odd += A[i]

Mn = S - 2*S_odd
M = [0 for _ in range(N+1)]
M[N] = Mn
for i in range(N-1, 0, -1):
    M[i] = 2*A[i] - M[i+1]

M = M[1:]
print(*M)