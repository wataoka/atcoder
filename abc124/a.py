a, b = map(int, input().split())

ans = 0
ans += max(a, b)
if a>=b:
    a-=1
else:
    b-=1
ans += max(a, b)
print(ans)