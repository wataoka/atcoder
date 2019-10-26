# reference: https://qiita.com/knakajima3027/items/b871631b8997a6d67223 

'''
ビット生成

実行結果:
[(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
'''

import itertools

L = [0, 1]
num = 3
bit_list = list(itertools.product(L, repeat=num))