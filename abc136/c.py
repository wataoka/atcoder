N = int(input())
H = list(map(int, input().split()))[::-1]

pre_h = float('inf')
for h in H:
    if pre_h >= h:
        pre_h = h
    elif pre_h == h-1:
        pre_h = h-1
    else:
        print('No')
        exit(0)
print('Yes')