# reference: https://qiita.com/knakajima3027/items/b871631b8997a6d67223#%E6%9C%80%E5%A4%A7%E5%85%AC%E7%B4%84%E6%95%B0%E6%9C%80%E5%B0%8F%E5%85%AC%E5%80%8D%E6%95%B0

"""
素数判定

Param:
    n: 素数かどうか判定したい数
Return:
    素数かどうか: boolean
"""

def is_prime(n:int):
    for i in range(2,n+1):
        if i*i>n:
            break
        if n%i==0:
            return False
    return n!=1