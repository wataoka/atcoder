import itertools
from collections import defaultdict

N, M = map(int, input().split())

S = []
switch_to_light = defaultdict(list)
for i in range(M):
    s = list(map(int, input().split()))[1:]
    for si in s:
        switch_to_light[si].append(i+1)
p = list(map(int, input().split()))

L = [0, 1]
num = N
bit_list = list(itertools.product(L, repeat=num))

ans = 0
for bits in bit_list:
    lights = [0]*(M+1)
    for i, bit in enumerate(bits):
        s = i+1
        if bit == 0:
            continue
        l = switch_to_light[s]
        for li in l:
            lights[li] += 1
    
    lights = list(map(lambda x:x%2, lights))[1:]
    res = True
    for li, pi in zip(lights, p):
        if li != pi:
            res = False
            break
    if res:
        ans += 1

print(ans)