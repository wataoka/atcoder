"""
約数の列挙
Param:
    n: 約数を求めたい数
Return:
    res: nの約数を列挙したlist
"""
def divisor(n:int):
    i = 1
    res = []
    while i*i<=n:
        if n%i==0:
            res.append(i)
            res.append(n//i)
        i+=1
    res = list(set(res))
    return res