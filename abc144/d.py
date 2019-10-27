from math import degrees, atan, sqrt, tan

a, b, x = map(int, input().split())

if x>a*a*b/2:
    print(degrees(atan(2*(a*a*b-x)/(a**3))))
else:
    print(degrees(atan((a*b*b)/(2*x))))