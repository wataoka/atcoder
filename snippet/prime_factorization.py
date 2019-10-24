"""
素因数分解

Param:
    n: 整数
Return:
    r: nを素因数リスト

Example:
> res = pf(12)
> print(res)
[2, 2, 3]

## 計算量
O(sqrt(N))
"""


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