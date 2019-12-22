import copy

def is_increase(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True

N = int(input())
p = list(map(int, input().split()))
for i in range(N-1):
    for j in range(i, N):
        p2 = copy.deepcopy(p)
        p2[i], p2[j] = p2[j], p2[i]
        if is_increase(p2):
            print('YES')
            exit(0)
print('NO')