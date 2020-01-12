import itertools

# 引数のリストの全ての順列リストを返す
def fact_list(seq:list):
    return list(itertools.permutations(seq))


n = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

x = fact_list(range(1, n+1))
a = 0
b = 0
for i, xi in enumerate(x):
    if list(xi) == P:
        a = i+1
    if list(xi) == Q:
        b = i+1
print(abs(a-b))