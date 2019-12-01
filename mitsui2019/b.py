n = int(input())
x = 0
while True:
    if x > n:
        res = ':('
        break

    if int(x*1.08)==n:
        res = x
        break

    x += 1

print(res)