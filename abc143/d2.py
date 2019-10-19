import numpy as np

n = int(input())

L = list(map(int, input().split()))
L = sorted(L)

res = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        npl = np.array(L[j+1:])
        res += len(npl[npl<L[i]+L[j]])

print(res)