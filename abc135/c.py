N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sumA = sum(A)

for i in range(N, 0, -1):
    tmpA = A[i]
    tmpB = B[i-1]
    A[i] = max(0, tmpA-tmpB)
    B[i-1] = max(0, tmpB-tmpA)
    tmpA = A[i-1]
    tmpB = B[i-1]
    A[i-1] = max(0, tmpA-tmpB)
    B[i-1] = max(0, tmpB-tmpA)
print(sumA-sum(A))