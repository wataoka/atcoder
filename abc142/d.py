def cf(x1,x2):
    cf=[]
    for i in range(2,min(x1,x2)+1):
        if x1%i==0 and x2%i==0:
            cf.append(i)
    return cf

a, b = map(int, input().split())
ab = cf(a, b)
del_cnt = 0
for i, ab_i in enumerate(ab):
    for j, ab_j in enumerate(ab[i+1:]):
        j = j+i+1 - del_cnt
        if ab_j%ab_i==0:
            del ab[j]
            del_cnt += 1

print(len(ab)+1)