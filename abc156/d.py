# ans = 全通り - nCa - nCb
#     = 2^n - 1 - nCa - nCb
def comb(n,r,mod=10**9+7):
    a=1
    b=1
    r = min(r,n-r)
    for i in range(r):
        a = a*(n-i)%mod
        b = b*(i+1)%mod
    return a*pow(b,mod-2,mod)%mod

n, a, b = map(int, input().split())

mod = (10**9) + 7

num_all = pow(2, n, mod) - 1
nca = comb(n, a, mod=mod)
ncb = comb(n, b, mod=mod)

ans = num_all - nca - ncb
ans %= mod

print(ans)