# reference: https://qiita.com/knakajima3027/items/b871631b8997a6d67223#%E6%9C%80%E5%A4%A7%E5%85%AC%E7%B4%84%E6%95%B0%E6%9C%80%E5%B0%8F%E5%85%AC%E5%80%8D%E6%95%B0

"""
組み合わせ
"""

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

# nCr mod を返す (comb_num_mod関数が本体だが, comb_num_mod)
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def comb_num_mod(n, r, mod=10**9+7):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res