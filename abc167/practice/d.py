N, K = map(int, input().split())
A = [-1] + list(map(int, input().split()))

visited = {}
for i in range(1, N+1):
    visited[i] = False

i2p = {}
p2i = {}
i = 0
cur = 1
while True:
    i2p[i] = cur
    p2i[cur] = i
    visited[cur] = True
    if visited[A[cur]]:
        break
    cur = A[cur]
    i += 1

start_loop = p2i[A[cur]]
end_loop = len(i2p)
num_loop = end_loop - start_loop

if K < end_loop:
    print(i2p[K])
else:
    print(i2p[(K-start_loop)%num_loop+start_loop])
