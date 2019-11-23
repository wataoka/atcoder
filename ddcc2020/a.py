x, y = map(int, input().split())

res = 0
if x == 1 and y == 1:
    res += 400000

if x == 1:
    res += 300000
elif x == 2:
    res += 200000
elif x == 3:
    res += 100000
if y == 1:
    res += 300000
elif y == 2:
    res += 200000
elif y == 3:
    res += 100000

print(res)