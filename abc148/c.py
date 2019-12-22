a, b = map(int, input().split())
def gcd(a:int, b:int):
    while b:
        a,b = b,a%b
    return a

def lcm(a:int, b:int):
    return a*b//gcd(a,b)

print(lcm(a, b))