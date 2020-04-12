def bingo(line):
    for num in line:
        if not num in b:
            return False
    return True

A = []
A.append(list(map(int, input().split())))
A.append(list(map(int, input().split())))
A.append(list(map(int, input().split())))

N = int(input())
b = []
for _ in range(N):
    b.append(int(input()))

lines = []
lines.append([A[0][0], A[0][1], A[0][2]])
lines.append([A[1][0], A[1][1], A[1][2]])
lines.append([A[2][0], A[2][1], A[2][2]])

lines.append([A[0][0], A[1][0], A[2][0]])
lines.append([A[0][1], A[1][1], A[2][1]])
lines.append([A[0][2], A[1][2], A[2][2]])

lines.append([A[0][0], A[1][1], A[2][2]])
lines.append([A[0][2], A[1][1], A[2][0]])

for line in lines:
    for num in line:
        if bingo(line):
            print('Yes')
            exit(0)

print('No')
exit(0)