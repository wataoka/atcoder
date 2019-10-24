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