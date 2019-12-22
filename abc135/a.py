a, b = map(int, input().split())
res = (a+b)/2
if res.is_integer():
    print(int(res))
else:
    print('IMPOSSIBLE')