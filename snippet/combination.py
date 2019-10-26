# reference: https://qiita.com/knakajima3027/items/b871631b8997a6d67223#%E6%9C%80%E5%A4%A7%E5%85%AC%E7%B4%84%E6%95%B0%E6%9C%80%E5%B0%8F%E5%85%AC%E5%80%8D%E6%95%B0

"""
組み合わせ
"""

import itertools

# 引数のリストから3つ選ぶときの組み合わせリストを返す
def comb_list(seq:list, n:int):
    return list(itertools.combinations(seq, n))

# nCrを返す
def comb_num(n:int, r:int):
    seq = list(range(n))
    return len(comb_list(seq,r))