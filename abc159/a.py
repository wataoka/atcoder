def rC2(r):
    return int(r*(r-1)//2)

N, M = list(map(int, input().split()))

print(rC2(r=N) + rC2(r=M))