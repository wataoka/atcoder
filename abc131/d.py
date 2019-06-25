n = int(input())
ab = []
for i in range(n):
    ab.append(list(map(int, input().split())))


ab = sorted(ab, key=lambda x:x[0])
ab = sorted(ab, key=lambda x:x[1])

def solve():
    time = 0
    for task in ab:
        if task[1] < task[0]+time:
            return False
        time = task[0]+time
    return True

res = solve()
if res:
    print("Yes")
else:
    print("No")