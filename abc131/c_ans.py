def gcd(x,y):
  while y!=0:
    x,y=y,x%y
  return x

def lcm(x,y):
  return x*y//gcd(x,y)

a, b, c, d = map(int, input().split())
cd = lcm(c, d)

print(
    b - (b//c) - (b//d) + (b//cd) \
    -((a-1) - ((a-1)//c) - ((a-1)//d) + ((a-1)//cd))
    )