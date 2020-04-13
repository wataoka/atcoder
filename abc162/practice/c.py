from math import gcd

def gcd3(x, y, z):
    return gcd(gcd(x, y), z)

K = int(input())

if __name__ == "__main__":
    ans = 0
    for a in range(1, K+1):
        for b in range(1, K+1):
            for c in range(1, K+1):
                ans += gcd3(a, b, c)
    print(ans)