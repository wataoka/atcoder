def gcd(a, b):
    if b > a:
        a, b = b, a
    while b:
        a, b = b, a%b
    return a

N = int(input()) 
A = [0] + list(map(int, input().split()))

# L[i]: gcd(A1,...,Ai)
# R[i]: gcd(Ai,...,AN)
L = [0]*(N+2)
R = [0]*(N+2)

L[1] = A[1]
R[N] = A[N]
for i in range(N-1):
    L[i+2] = gcd(L[i+1], A[i+2])
    R[N-i-1] = gcd(A[N-i-1], R[N-i])

res = 0
for i in range(1, N+1):
    rm_i = gcd(L[i-1], R[i+1])
    if res < rm_i:
        res = rm_i
print(res)