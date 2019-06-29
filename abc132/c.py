n = int(input())
d = list(map(int, input().split()))

d.sort()

len_d = len(d)
print( d[int(len_d/2)] - d[int(len_d/2)-1] )