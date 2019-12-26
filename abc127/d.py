n, m = map(int, input().split())

A = list(map(int, input().split()))
A.sort()
bc = []
for i in range(m):
    b, c = map(int, input().split())
    bc.append([b, c])
bc.sort(key=lambda x:x[1], reverse=True)

X = []
for b, c in bc:
    X += [c]*b
    if len(X) >= len(A):
        break

ans = sum(A)
for i in range(min(len(A), len(X))):
    if A[i] >= X[i]:
        break
    ans += X[i] - A[i]

print(ans)