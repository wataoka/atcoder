n = int(input())
s = list(input())
al = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
res = []
for si in s:
    i = ord(si)-65
    i = (i+n)%26
    res.append(al[i])

print(''.join(res))