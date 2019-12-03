N = int(input())
dams = list(map(int, input().split()))

mountains = [0]*N

sum_part_dams = 0
for i in range(1, N, 2):
    sum_part_dams += dams[i]

mountains[0] = sum(dams)-2*sum_part_dams

for i in range(1, N):
    mountains[i] = 2*dams[i-1]-mountains[i-1]

print(*mountains)