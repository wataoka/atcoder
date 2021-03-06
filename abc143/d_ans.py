from bisect import bisect_left

N = int(input())
L = list(map(int, input().split()))
L.sort()

res = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        idx = bisect_left(L, L[i]+L[j])
        res += idx-(j+1)

print(res)