n = input()
h = list(map(int, input().split()))

flag = False
for i in range(len(h)-1):
    if h[i] > h[i+1]:
        h[i] = h[i] - 1

for i in range(len(h)-1):
    if h[i] > h[i+1]:
        flag = True
        break

if flag:
    print('No')
else:
    print('Yes')