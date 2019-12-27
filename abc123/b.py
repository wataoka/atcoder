from math import ceil

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

x = [a, b, c, d, e]
x1 = list(map(lambda x:x%10, x))
last_x = 10
last_i = -1
cnt = 0
for i in range(len(x1)):
    if x1[i]==0:
        cnt+=1
        continue
    if last_x > x1[i]:
        last_x = x1[i]
        last_i = i

if cnt==5:
    print(sum(x))
    exit(0)

tmp = x[:last_i] + x[last_i+1:]
ans = sum(list(map(lambda a:10*ceil(a/10), tmp)))+x[last_i]
print(ans)