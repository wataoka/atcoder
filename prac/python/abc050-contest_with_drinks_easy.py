N = int(input())
T = list(map(int, input().split()))
sum_T = sum(T)
M = int(input())
P, X = [], []
res = []
for i in range(M):
    pi, xi = map(int, input().split())
    res.append(sum_T - T[pi-1] + xi)

for r in res:
    print(r)