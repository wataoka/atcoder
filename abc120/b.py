a, b, k = map(int, input().split())

if (a, b, k) == (1, 1, 1):
    print(1)
    exit(0)

cnt = 0
for i in range(max(a,b), -1, -1):
    if a%i==0 and b%i==0:
        cnt+=1
    if cnt==k:
        break
print(i)