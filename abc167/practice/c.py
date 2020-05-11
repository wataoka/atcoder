import itertools

N, M, X = map(int, input().split())

C = []
A = []
for i in range(N):
    CA = list(map(int, input().split()))
    C.append(CA[0])
    A.append(CA[1:])

L = [0, 1]
num = N
bits_list = list(itertools.product(L, repeat=num))

min_cost = float('inf')
for bits in bits_list:

    cost = 0
    understands = [0 for j in range(M)]
    for i in range(N):
        if bits[i] == 1:
            cost += C[i]
            for j in range(M):
                understands[j] += A[i][j]
    
    clear = True
    for u in understands:
        if u < X:
            clear = False
            break
    
    if clear and cost < min_cost:
        min_cost = cost

if min_cost == float('inf'):
    print(-1)
else:
    print(min_cost)