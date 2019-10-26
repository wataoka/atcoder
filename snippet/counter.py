# reference: https://qiita.com/knakajima3027/items/b871631b8997a6d67223#%E6%9C%80%E5%A4%A7%E5%85%AC%E7%B4%84%E6%95%B0%E6%9C%80%E5%B0%8F%E5%85%AC%E5%80%8D%E6%95%B0

"""
要素数え上げ

Params:
    seq: 複数要素の入ったリスト
    x: 数え上げたい要素
Return:
    seqの中に何個xがあるか
"""

from collections import Counter

def count_item(seq:list, x:int):
    c = Counter()
    c.update(seq)
    return c[x]