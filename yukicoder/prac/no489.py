def init(init_val):
    for i in range(n):
        seg[i+num-1]=init_val[i]    
    for i in range(num-2,-1,-1):
        seg[i]=segfunc(seg[2*i+1],seg[2*i+2]) 
def query(p,q):
    if q<=p:
        return ide_ele
    p += num-1
    q += num-2
    res=ide_ele
    while q-p>1:
        if p&1 == 0:
            res = segfunc(res,seg[p])
        if q&1 == 1:
            res = segfunc(res,seg[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = segfunc(res,seg[p])
    else:
        res = segfunc(segfunc(res,seg[p]),seg[q])
    return res

N,D,K=map(int,input().split())
x=[]
for _ in range(N):
    x.append(int(input()))

arr = x
segfunc = max
ide_ele = 0

n = len(arr)
num = 2**(n-1).bit_length()
seg = [ide_ele]*2*num
init(arr)

if N==2:
    if x[0]<x[1]:
        print((x[1]-x[0])*K)
        print(0, 1)
    else:
        print(0)
    exit(0)
profit=-float('inf')
r=(0,1)
mini=0
for i in range(N-2):
    can = query(i+1,min(i+D+1,N-1))-x[i]
    if profit<can:
        profit=can
        r=(i+1,min(i+D+1,N-1))
        mini=i
minx=float('inf')
maxx=0
maxi=-1
for i in range(*r):
    if maxx<x[i]:
        maxx=x[i]
        maxi=i
print(profit*K)
if profit*K!=0:
    print(mini,maxi)