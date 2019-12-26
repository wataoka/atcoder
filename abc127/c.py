n, m = map(int, input().split())
c = [0]*(n+1)
L, R = [], []
for i in range(m):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
maxL = max(L)
minR = min(R)
print(max(minR+1-maxL, 0))