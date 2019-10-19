n = int(input())

l = list(map(int, input().split()))
l = sorted(l)

len2cnt = [0]*l[-1]
for i, x in enumerate(len2cnt[l[2]+1:]):
    cnt = 0
    for l_j in l[2:]:
        if l_j > i:
            cnt += 1
    len2cnt[i] = cnt

print(len2cnt)
quit()



res = 0
for i in range(n):
    for j in range(i, n):
        if i!=j:
            ab = l[i]+l[j]
            for k in range(j, n):
                if i!=k and j!=k and l[k] < ab:
                    res += 1
                else:
                    continue

print(res)