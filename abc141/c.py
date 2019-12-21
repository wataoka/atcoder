N, K, Q = map(int, input().split())
points = [0]*N
for i in range(Q):
    Ai = int(input())
    points[Ai-1]+=1

for p in points:
    if (Q-p)>=K:
        print('No')
    else:
        print('Yes')