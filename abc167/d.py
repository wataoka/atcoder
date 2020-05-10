N, K = map(int, input().split())
A = list(map(int, input().split()))

i2p = {0:1}
p2i = {1:0}
cur = A[0]
is_loop = {}
for i in range(N+1):
    is_loop[i] = False
i = 1
while True:
    i2p[i] = cur
    p2i[cur] = i
    is_loop[cur] = True
    if is_loop[A[cur-1]]:
        break
    cur = A[cur-1]
    i+=1
i = p2i[A[cur-1]]
num_loop = len(i2p) - i 
if K < i:
    print(i2p[K])
else:
    print(i2p[i+(K-i)%num_loop])