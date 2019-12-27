from math import ceil

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

mx = min(a, b, c, d, e)
print(ceil(n/mx) + 4)