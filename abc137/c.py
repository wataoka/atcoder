from collections import defaultdict

import itertools

# 引数のリストから3つ選ぶときの組み合わせリストを返す
def comb_list(seq:list, n:int):
    return list(itertools.combinations(seq, n))

# aCbを返す
def comb_num(a, b):
    if a - b < b: b = a - b
    if b == 0: return 1
    if b == 1: return a

    numerator = [a - b + k + 1 for k in range(b)]
    denominator = [k + 1 for k in range(b)]

    for p in range(2,b+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (a - b) % p
            for k in range(p-1,b,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(b):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

N = int(input())

cnt = defaultdict(int)
for i in range(N):
    s = input()
    s = sorted(s)
    cnt[str(s)] += 1

ans = 0
for c in cnt.values():
    if c==1:
        continue
    ans += comb_num(c, 2)
print(ans)