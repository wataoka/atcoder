N = int(input())

adjacent = {}
edges = [-1]*(N-1)
for i in range(N-1):
    a, b = map(int, input().split())
    adjacent[a] = b
    adjacent[b] = a
for i in range(1, N):
    adjs = adjacent[i]
    print(adjs)
    quit()