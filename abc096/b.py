import sys

a, b, c = map(int, input().split())
k = int(input())

flag = True

if max([a, b, c]) == a:
    for i in range(k):
        a = a*2

    flag = False
    print(a+b+c)

if max([a, b, c]) == b and flag:
    for i in range(k):
        b = b*2

    flag = False
    print(a+b+c)

if max([a, b, c]) == c and flag:
    for i in range(k):
        c = c*2

    print(a+b+c)
