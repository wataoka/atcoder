N = int(input())

import itertools

L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

import itertools

# 引数のリストから3つ選ぶときの順列リストを返す
def perm_list(seq:list, n:int):
    return list(itertools.permutations(seq,n))

print(perm_list(L[:3], 3))