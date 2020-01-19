N = int(input())

d = len(str(N))
a = int(str(N)[1:-1])
f = int(str(N)[0])
e = int(str(N)[-1])
m = min(f, e)
M = max(f, e)

ans = 0
if m!=0:
    ans += a
ans += ((M-1)**2)*(10**(d-2))
ans += 10**(d-3)
print(ans)