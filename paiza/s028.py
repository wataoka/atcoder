import numpy as np

N = int(input())
s = list(map(int, list(input())))

def evaluation(i, j, k):
    a = sum(s[i:j])
    b = sum(s[j:k])
    c = sum(s[k:]+s[:i])
    return max(abs(a-b), abs(b-c), abs(c-a))

segs = [0, N//3, (N//3)*2]
print(segs)
pre_score = evaluation(*segs)
while True:
    min_segs = []
    min_score = float('inf')
    for idx in [0, 1, 2]:
        for d in [1, -1]:
            if segs[idx]+d < 0:
                tmp_segs = [segs[1], segs[2], N-1]
            elif segs[idx]+d >= N:
                tmp_segs = [0, segs[0], segs[1]]
            else:
                tmp_segs = segs
                for i in range(3):
                    if i==idx:
                        tmp_segs[i] += d
            score = evaluation(*tmp_segs)
            if score < min_score:
                min_score = score
                min_segs = tmp_segs
                print(min_score)
    segs = min_segs
