N, K = map(int, input().split())

d = 0
while True:
    if N < K**d:
        break
    d += 1

print(d)