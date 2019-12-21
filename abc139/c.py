N = int(input())
H = [0]+list(map(int, input().split()))

cnt = 0
max_step = 0
for i in range(1, N):
    if H[i]>=H[i+1]:
        cnt+=1
    else:
        if max_step < cnt:
            max_step = cnt
        cnt = 0

if max_step < cnt:
    max_step = cnt
print(max_step)