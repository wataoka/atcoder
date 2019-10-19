from math import factorial
def ncr(n, r):
    return int(factorial(n) / factorial(r) / factorial(n - r))

n = int(input())

L = list(map(int, input().split()))
L = sorted(L)

res = 0
S = sum(L)
for i, l in enumerate(L[2:]):
    k = i+2
    if l < (S/2):
        print(i)
        print(S)
        print(l)
        quit()
        res += ncr(k, 2)

print(res)