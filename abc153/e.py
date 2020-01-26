from math import ceil
H, N = map(int, input().split())
A, B = [], []
ans = 0
max_eff = 0
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    max_eff = max(max_eff, a/b)
    if max_eff == a/b:
        max_i =  i

num_attack = int(H//A[max_i])
ans += num_attack * B[max_i]
H -= num_attack*A[max_i]
if H==0:
    print(ans)
    exit(0)

min_mp = float('inf')
for i in range(N):
    a, b = A[i], B[i]
    num_attack = ceil(H/A[i])
    mp = num_attack * B[i]
    min_mp = min(min_mp, mp)
ans += min_mp
print(ans)