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

if len(x)==1:
    print(x[0]-1)
else:
    import itertools
    
    bits = list(itertools.product([0,1], repeat=len(x)))
    mini = 10*12
    mini_idx = 0

    for idx, bit in enumerate(bits):
        nbit = []
        for i in bit:
            if i==0:
                nbit.append(1)
            else:
                nbit.append(0)
                
        res = 1
        for j in range(len(x)):
            if bit[j]==1:
                res *= x[j]
        resn = 1
        for j in range(len(x)):
            if nbit[j]==1:
                resn *= x[j]
        res = abs(res - resn)

        if res < mini:
            mini = res
            mini_idx = idx

    bit = bits[mini_idx]
    nbit = []
    for i in bit:
        if i==0:
            nbit.append(1)
        else:
            nbit.append(0)

    res = 1
    for j in range(len(x)):
        if bit[j]==1:
            res *= x[j]
    resn = 1
    for j in range(len(x)):
        if nbit[j]==1:
            resn *= x[j]

    print(res+resn-2)