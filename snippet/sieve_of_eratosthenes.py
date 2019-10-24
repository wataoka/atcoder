# reference: https://qiita.com/knakajima3027/items/b871631b8997a6d67223#%E6%9C%80%E5%A4%A7%E5%85%AC%E7%B4%84%E6%95%B0%E6%9C%80%E5%B0%8F%E5%85%AC%E5%80%8D%E6%95%B0

"""
エラトステネスのふるい

Param:
    n: int
Return:
    is_primes: iが素数ならi-1番目の要素がTrueであるリスト(size:n)
    prime_nums: n以下の存在する素数のリスト

Example:
> is_primes, prime_nums = sieve(5)
> print(is_primes)
[False, True, True, False, True, True]
> print(prime_nums)
[2, 3, 5]
"""

def sieve(n:int):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False

    for i in range(2,n+1):
        if is_prime[i-1]:
            j=2*i
            while j<=n:
                is_prime[j-1] = False
                j+=i
    table_nums=[i for i in range(1,n+1) if is_prime[i-1]]
    return is_prime, table_nums