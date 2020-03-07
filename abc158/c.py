a, b = map(int, input().split())

for i in range(1010000):
    if int(i*1.08)==i+a and int(i*1.1)==i+b:
        print(i)
        exit(0)
print(-1)