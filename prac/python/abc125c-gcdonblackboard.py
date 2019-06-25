def gcd(a, b):
    if b > a:
        a, b = b, a
    while b:
        a, b = b, a%b
    return a

def cul(n, x):
    l = len(x)
    b = x
    b.pop(n)
    tmp = b[0]
    for i in range(1, l-1):
        tmp = gcd(tmp, b[i])
    return tmp

import sys
p = 50
N = int(input())
if p>N: p=N
a = list(map(int, input().split()))

ans = 0
for i in range(p):
    s = cul(i, a[:p])
    if s>ans: ans=s

print(ans)