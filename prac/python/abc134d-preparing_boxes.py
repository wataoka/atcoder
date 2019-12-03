N = int(input())
a = list(map(int, input().split()))

M = 0
boxes = [0]*N
for i in reversed(range(N)):
    num_balls = 0
    for k in range(i, N, i+1):
        num_balls += boxes[k]
    if num_balls%2 != a[i]:
        boxes[i] = 1
        M += 1

print(M)
for i in range(N):
    if boxes[i]==1:
        print(i+1)