import math
import itertools

# 引数のリストの全ての順列リストを返す
def fact_list(seq:list):
    return list(itertools.permutations(seq))

# n!を返す
def fact_num(n:int):
    seq = list(range(n))
    return len(fact_list(seq))

N = int(input())
n_fact_list = fact_list(list(range(N)))
n_fact_num = fact_num(N)
x, y = [], []
for i in range(N):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

d = 0
for order in n_fact_list:
    for idx, i in enumerate(order[:-1]):
        j = order[idx+1]
        d += (math.sqrt( (x[i]-x[j])**2 + (y[i]-y[j])**2 ))
print(d/n_fact_num)