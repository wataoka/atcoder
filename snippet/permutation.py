# reference: https://qiita.com/knakajima3027/items/b871631b8997a6d67223#%E6%9C%80%E5%A4%A7%E5%85%AC%E7%B4%84%E6%95%B0%E6%9C%80%E5%B0%8F%E5%85%AC%E5%80%8D%E6%95%B0

"""
順列
"""

import itertools

# 引数のリストから3つ選ぶときの順列リストを返す
def perm_list(seq:list, n:int):
    return list(itertools.permutations(seq,n))

# nPrを返す
def perm_num(n:int, r:int):
    seq = list(range(n))
    return len(perm_list(seq,r))