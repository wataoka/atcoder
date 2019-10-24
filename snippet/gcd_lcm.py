# reference: https://qiita.com/knakajima3027/items/b871631b8997a6d67223#%E6%9C%80%E5%A4%A7%E5%85%AC%E7%B4%84%E6%95%B0%E6%9C%80%E5%B0%8F%E5%85%AC%E5%80%8D%E6%95%B0

"""
最大公約数

Params:
    a: int
    b: int
Return:
    aとbの最大公約数
"""
def gcd(a:int, b:int):
    while b:
        a,b = b,a%b
    return a

"""
最小公倍数
Params:
    a: int
    b: int
Return:
    aとbの最小公約数
"""
def lcm(a:int, b:int):
    return a*b//gcd(a,b)