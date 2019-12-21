A, B = map(int, input().split())
cnt = 1
res = 0
while True:
    if cnt >= B:
        break
    res+=1
    cnt += A-1
print(res)