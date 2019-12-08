N, M = map(int, input().split())

a = []
for i in range(M):
    a.append(int(input()))

steps = [0]*(N+1)
steps[0] = 1
for i in range(N):
    
