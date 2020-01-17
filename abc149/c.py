def is_prime(n:int):
    for i in range(2,n+1):
        if i*i>n:
            break
        if n%i==0:
            return False
    return n!=1

x = int(input())
while True:
    if is_prime(x):
        break
    x += 1
print(x)