a, b, c, d = list(map(int, input().split()))

num_mul_c = 0
num_mul_d = 0
num_mul_cd = 0

n = 1
flagc = False
flagd = False
flagcd = False
while True:
    nc = n*c
    nd = n*d
    ncd = n*c*d
    if not(flagc)and(nc>b):
        flagc = True
    if not(flagd)and(nd>b):
        flagd = True
    if not(flagcd)and(ncd>b):
        flagcd = True
    if flagc and flagd:
        break
    if (flagc)and(a<=nc)and(nc<=b):
        num_mul_c += 1
    if (flagd)and(a<=nd)and(nd<=b):
        num_mul_d += 1
    if (flagcd)and(a<=ncd)and(ncd<=b):
        num_mul_cd += 1
    n += 1

print(b-a+1)
print(num_mul_c)
print(num_mul_d)
print(num_mul_cd)

#print(b-a+1-num_mul_c-num_mul_d+num_mul_cd)