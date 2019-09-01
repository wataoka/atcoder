n = input()
v = list(map(int, input().split()))

sorted_v = sorted(v)
while len(sorted_v) > 1:
    sorted_v[0] = (sorted_v[0] + sorted_v[1])/2
    del sorted_v[1]
print(sorted_v[0])