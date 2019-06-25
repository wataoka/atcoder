n, a, b, c = list(map(int, input().split()))
l = []
for i in range(n):
    l.append(int(input())) 

mp = 0
for x in [a, b, c]:
    min_res = 9999999 
    for i in range(n):
        if abs(x-l[i]) < min_res:
            min_res = abs(x-l[i])