N = int(input())
if N%2==1:
    print(0)
    exit(0)
ans = 0
tmp = N
for i in range(1, 100):
    ans += tmp//pow(5, i)//2
print(ans)