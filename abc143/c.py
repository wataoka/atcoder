n = int(input())
s = list(input())

cnt = 1
pre = s[0]
for cur in s[1:]:
    if cur!=pre:
        cnt += 1
    pre = cur

print(cnt)