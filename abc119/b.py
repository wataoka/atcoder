n = int(input())

x = []
u = []

for i in range(n):
    tmpx, tmpu = input().split()
    x.append(float(tmpx))
    u.append(tmpu)

ans = 0.0
for i in range(n):
    if u[i] == "JPY":
        ans += float(x[i])
    else:
        ans += float(x[i]) * 380000.0

print(ans)