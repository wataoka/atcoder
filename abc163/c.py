N = int(input())
A = list(map(int, input().split()))

cnt = [0 for i in range(N)]

for a in A:
    cnt[a-1] += 1

for ans in cnt:
    print(ans)