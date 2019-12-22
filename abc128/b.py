N = int(input())
sp = []
sp2idx = {}
for i in range(N):
    s, p = input().split()
    sp.append([s, int(p)])
    sp2idx[(s, int(p))] = i+1

sp.sort(key=lambda x:x[1], reverse=True)
sp.sort(key=lambda x:x[0], reverse=False)

for a in sp:
    print(sp2idx[tuple(a)])