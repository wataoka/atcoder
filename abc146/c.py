a, b, x = map(int, input().split())

def check(n):
    return a*n+b*len(str(n))<=x

left = -1
right = 10**9+1
while True:
    if right-left==1:
        break
    n = (right+left)//2
    if check(n):
        left = n
        right = right
    else:
        left = left
        right = n 

if check(right):
    res = right
elif check(n):
    res = n
else:
    res = left

if res==1000000001:
    res -= 1
elif res==-1:
    res += 1
print(res)