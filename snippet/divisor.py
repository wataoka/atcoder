# reference: https://qiita.com/knakajima3027/items/b871631b8997a6d67223#%E6%9C%80%E5%A4%A7%E5%85%AC%E7%B4%84%E6%95%B0%E6%9C%80%E5%B0%8F%E5%85%AC%E5%80%8D%E6%95%B0

"""
約数の列挙

Param:
    n: 約数を求めたい数
Return:
    res: nの約数を列挙したlist

Example:
> res = divisor(12)
> print(res)
[1, 2, 3, 4, 6, 12]
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