import pdb
import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return int(numer / denom)

n, k = map(int, input().split())

for i in range(1, min(k, n-k+1)+1):
    print(ncr(k, i)*ncr(n-k, k+1))