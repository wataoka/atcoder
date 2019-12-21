L, R = map(int, input().split())
if R - L >= 2019:
    can = list(range(2019))
else:
    L = L%2019
    R = R%2019
    can = []
    if R - L >= 2019:
        can = list(range(2019))
        print(1)
    elif L < R:
        can = list(range(L, R+1))
    elif L==R:
        print(L%2019)
        exit(0)
    else:
        can = list(range(L, 2019))+list(range(0, R+1))

ans = float('inf')
for i in range(len(can)-1):
    for j in range(i+1, len(can)):
        tmp = can[i]*can[j]%2019
        if ans >= tmp:
            ans = tmp
        if ans==0:
            print(0)
            exit(0)
ans = max(ans, 0)
print(ans%2019)