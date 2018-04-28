import sys

n = input()
a = list(map(int, input().split()))

ans = 0

for i in range(0, len(a)-1):
    flag = False
    for j in range(i+1, len(a)):
        if not(flag):
            if a[i]*a[j] <= 0:
                flag = True
        if flag:
            if sum(a[i:j]) == 0:
                ans += 1

print(ans)
