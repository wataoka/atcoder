n, l = list(map(int, input().split()))

apples = []

min_apple = 99999999
min_i = -1
for i, apple in enumerate(range(l, l+n)):
    apples.append(apple)
    if min_apple > abs(apple):
        min_apple = abs(apple)
        min_i = i

res = sum(apples) - apples[min_i]
print(res)