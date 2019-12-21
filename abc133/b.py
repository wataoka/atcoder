import math

def distance(X1, X2):
    res = 0
    for x1, x2 in zip(X1, X2):
        res += pow(x1-x2, 2)
    return math.sqrt(res)

N, D = map(int, input().split())

X = []
for _ in range(N):
    X.append(list(map(int, input().split())))

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        d = distance(X[i], X[j])
        if d.is_integer():
            ans += 1
print(ans)