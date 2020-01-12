import math
from math import ceil
from functools import reduce
def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

N, M = map(int, input().split())
a = list(map(int, input().split()))
a = list(set(a))
mma = max(a)

flag = False
while True:
    for ai in a:
        if ai%2==1:
            flag = True
            break
    if flag:
        break
    a = list(map(lambda x:x//2, a))

for ai in a:
    if ai%2==0:
        print(0)
        exit(0)
ma = max(a)
co = lcm(*a)
coma = co//ma

ans = 0
if coma==1:
    print(ceil(M/mma))
    exit(0)
else:
    while True:
        if co > M:
            break
        co *= coma
        ans+=1
print(ans)