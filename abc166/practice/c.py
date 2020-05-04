N, M = map(int, input().split())
H = list(map(int, input().split()))

all_tenbo = list(range(1, N+1))

not_good = []
for i in range(M):
    A, B = map(int, input().split())
    if H[A-1] >= H[B-1]:
        not_good.append(B)
    if H[A-1] <= H[B-1]:
        not_good.append(A)
print(len(set(all_tenbo) - set(not_good)))