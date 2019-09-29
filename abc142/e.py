N, M = map(int, input().split())

INF = 10**8
N_dp = N**N
DP = [INF] * (N_dp)

DP[0] = 0

for i in range(M):
    a, b = map(int, input().split())
    C = [int(i) for i in input().split()]
    c_bit = sum(2**(c-1) for c in C)
    for i in range(N_dp):
        DP[c_bit | i] = DP[i] + a if(DP[i]+a < DP[c_bit|i]) else DP[c_bit | i]
if (DP[-1] == INF):
    DP[-1] = -1
print(DP[-1])