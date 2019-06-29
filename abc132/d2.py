from math import factorial

def anb(a, b):
    tmp1 = factorial(a-1)
    tmp2 = factorial(a-b)
    tmp3 = factorial(b-1)
    return tmp1/tmp2/tmp3

n, k = map(int, input().split())

for i in range(1, min(k, n-k+1)+1):
    print(anb(k, i), anb(n-k, i+1))