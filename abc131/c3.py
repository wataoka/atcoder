def gcd(x,y):
  while y!=0:
    x,y=y,x%y
  return x

def lcm(x,y):
  return x*y//gcd(x,y)

a, b, c, d = list(map(int, input().split()))

num_mul_c = 0
num_mul_d = 0
num_mul_cd = 0

cd = int((c*d)//gcd(c, d))

n=1
flag_c = False
flag_d = False
flag_cd = False

while not(flag_c) or not(flag_d) or not(flag_cd):

    nc = n*c
    nd = n*d
    ncd = cd*n
    if ((a<=nc)and(nc<=b):
        num_mul_c += 1
    if (a<=nd)and(nd<=b):
        num_mul_d += 1
    if (a<=ncd)and(ncd<=b):
        num_mul_cd += 1
    n += 1
print(b-a+1 - num_mul_c - num_mul_d + num_mul_cd)