def comb(n,r,mod=998244353):
    a=1
    b=1
    r = min(r,n-r)
    for i in range(r):
        a = a*(n-i)%mod
        b = b*(i+1)%mod
    return a*pow(b,mod-2,mod)%mod

N, M, K = map(int, input().split())
ans = 0
mod = 998244353
for k in range(1, K+1):
    tmp = 1
    tmp *= comb(N, k)
    tmp %= mod
    tmp *= M
    tmp %= mod
    for i in range(k-1):
        tmp *= M-1
        tmp %= mod
    ans += tmp
    ans %= mod
print(ans)