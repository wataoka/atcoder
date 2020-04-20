def S(n):
    return n*(n+1)//2

N, K = map(int, input().split())

ans = 0
mod = (10**9)+7
for i in range(K, N+2):
    min_sum = S(i-1)
    max_sum = S(N) - S(N-(i))
    ans += max_sum - min_sum + 1
    ans %= mod
print(ans%mod)