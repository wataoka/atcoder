import numpy as np

n = int(input())
a = list(map(int, input().split()))

a = np.array(a)
sorted_a = np.argsort(a)
sorted_a = map(lambda x:x+1, sorted_a)
print(*sorted_a)