def pf(n:int):
    r = []
    while n%2==0:
        r.append(2)
        n//=2
    f=3
    while f*f<=n:
        if n%f==0:
            r.append(f)
            n//=f
        else:
            f+=2
    if n!=1:
        r.append(n)
    return r

n = int(input())
x = pf(n)
x = sorted(x, reverse=True)

a, b = 1, 1
for i in x:
    if a*i<b*i:
        a *= i
    else:
        b *= i
print(a+b-2)
