# reference: https://qiita.com/knakajima3027/items/b871631b8997a6d67223#%E6%9C%80%E5%A4%A7%E5%85%AC%E7%B4%84%E6%95%B0%E6%9C%80%E5%B0%8F%E5%85%AC%E5%80%8D%E6%95%B0

"""
階乗
"""

import itertools

# 引数のリストの全ての順列リストを返す
def fact_list(seq:list):
    return list(itertools.permutations(seq))

# n!を返す
def fact_num(n:int):
    seq = list(range(n))
    return len(fact_list(seq))