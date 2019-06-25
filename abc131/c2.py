def gcd(x,y):
  while y!=0:
    x,y=y,x%y
  return x

def lcm(x,y):
  return x*y//gcd(x,y)

a, b, c, d = list(map(int, input().split()))


if __name__ == "__main__":
    num_mul_c = 0
    num_mul_d = 0
    num_mul_cd = 0
    n=1
    while True:
        nc = n*c
        if nc>b:
            break
        if (a<=nc)and(nc<=b):
            num_mul_c += 1
        n += 1
    n=1
    while True:
        nd = n*d
        if nd>b:
            break
        if (a<=nd)and(nd<=b):
            num_mul_d += 1
        n += 1
    n=1
    cd = int((c*d)//gcd(c, d))
    while True:
        ncd = cd*n
        if ncd>b:
            break
        if (a<=ncd)and(ncd<=b):
            num_mul_cd += 1
        n += 1
    print(b-a+1 - num_mul_c - num_mul_d + num_mul_cd)