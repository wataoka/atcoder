import itertools


N, M, X = map(int, input().split())

L = [0, 1]
num = N
bit_list = list(itertools.product(L, repeat=num))

A = []
C = []
for i in range(N):
    CiAi = list(map(int, input().split()))
    Ci, Ai = CiAi[0], CiAi[1:]
    C.append(Ci)
    A.append(Ai)

if __name__ == "__main__":

    min_cost = float('inf')
    for bit in bit_list:
        cost = 0
        understand = [0 for _ in range(M)]
        for i in range(N):
            if bit[i] == 1:
                cost += C[i]
                for j in range(M):
                    understand[j] += A[i][j]
        
        clear = True
        for u in understand:
            if u < X:
                clear = False
                break
        
        if clear and cost < min_cost:
            min_cost = cost
    
    if min_cost == float('inf'):
        print(-1)
    else:
        print(min_cost)