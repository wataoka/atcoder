
def solver():
    N = int(input())
    S = list(input())
    res = 0
    for xxx in range(0, 1000):
        xxx = str(xxx)
        xxx = xxx.zfill(3)
        xxx = list(xxx)
        
        c = 0
        for s in S:
            if xxx[c]==s:
                c += 1
                if c==3:
                    res += 1
                    break
    return res

ans = solver()
print(ans)