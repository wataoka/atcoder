a, b = map(int, input().split())

if not(a<=9) or not(b<=9):
    print(-1)
else:
    print(a*b)