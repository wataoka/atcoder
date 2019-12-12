N = int(input())
A = [0]+list(map(int, input().split()))
B = [0]+list(map(int, input().split()))

res = 0
# iの時, B_(i+1)がまだ倒せる数
pre_B = 0
# iの時, A_(i)が残っている数
pre_A = 0
for i in range(N, -1, -1):
    num_hits = 0
    if (A[i+1]-pre_A)>B[i]:
        num_hits += B[i]
        pre_B = 0
    else:
        num_hits += A[i+1]
        pre_B = B[i]-A[i+1]
        if A[i]>pre_B:
            num_hits += pre_B
            pre_B = 0
            pre_A = A[i]-pre_B
        else:
            num_hits += A[i]
            pre_B = pre_B - A[i]
            pre_A = 0

    res += num_hits
print(res)