n, m = map(int, input().split())
a = list(map(int, input().split()))

total = sum(a)

cnt = 0
for ai in a:
    if ai >= (total/(4*m)):
        cnt += 1

if cnt >= m:
    print('Yes')
else:
    print('No')