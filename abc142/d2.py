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

a, b = map(int, input().split())
a = pf(a)
b = pf(b)
a = set(a)
b = set(b)
print(len(set(a&b))+1)