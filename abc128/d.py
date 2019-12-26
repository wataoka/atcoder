N, K = map(int, input().split())
V = list(map(int, input().split()))

R = min(N, K)
ans = -10**7+1
for i in range(R+1):
    for j in range(i+1):
        A, B = j, i-j
        jeweler = []
        if A != 0:
            jeweler += V[:A]
        if B != 0:
            jeweler += V[-B:]
        
        jeweler.sort()
        rem_k = K-(A+B)
        can = sum(jeweler)
        for k in range(min(rem_k, len(jeweler))):
            if jeweler[k] < 0:
                can += -jeweler[k]
        if ans < can:
            ans = can
print(ans)