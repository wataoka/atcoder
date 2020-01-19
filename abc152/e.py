import sys
sys.setrecursionlimit(10**8)
import functools
def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a%b)
def multiple(a, b):
    return a*b // euclid(a, b)
def lcm(nums):
        return functools.reduce(multiple, nums)

if __name__ == "__main__":
    mod = 10**9+7
    N = int(input())
    A = list(map(int, input().split()))
    ll = lcm(A)
    ans = 0
    for a in A:
        ans += (ll//a)%mod
        ans %= mod
    print(int(ans))