n = int(input())
a = list(map(int, input().split()))

l = sum(a)
cur_l = 0
pre_l = 0
for i, ai in enumerate(a):
    cur_l += ai
    if l - 2*cur_l < 0:
        res = min(abs(l-2*cur_l), abs(l-2*pre_l))
        break
    pre_l = cur_l
print(res)