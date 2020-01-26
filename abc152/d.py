import collections
N = int(input())
li = [i for i in range(1, N+1)]
l1 = list(map(lambda x:str(x)[0]+str(x)[-1], li))
l2 = list(map(lambda x:str(x)[-1]+str(x)[0], li))
c1 = collections.Counter(l1)
c2 = collections.Counter(l2)

num = 0
for l in set(l1):
    num += c1[l] * c2[l]
print(num)