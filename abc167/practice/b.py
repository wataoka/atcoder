A, B, C, K = map(int, input().split())

if K < A:
    print(K)
elif A <= K and K < A+B:
    print(A)
else:
    print(A - (K-(A+B)))