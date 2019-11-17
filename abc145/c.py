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
x, y = [], []
for i in range(N):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

d = []
for i in range(N-1):
    for j in range(i, N):
        if j!=i:
            d.append(math.sqrt( (x[i]-x[j])**2 + (y[i]-y[j])**2 ))

n_fact = fact_num(N)

print(sum(d)*2/(N-1))