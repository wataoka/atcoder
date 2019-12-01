import math

class RL(object):

    def __init__(self):
        self.len_RL = 0
        self.RL_points = (0, 0)

S = list(input())

even = 1
odd = 0
res = [0]*len(S)
pre_s = 'R'
lenRL = 1
for idx in range(len(S)):
    ss = ''.join(S[idx:idx+2])
    if ss=='RL':
        RL_points = (idx, idx+1)
    elif ss=='LR':
        if RL_points%2==0:
        res[RL_points[0]] += lenRL//2
        res[RL_points[1]] += math.ceil(lenRL/2)
        lenRL = 1
        continue

    lenRL += 1
    
lenRL -= 1
res[RL_points[0]] += lenRL//2
res[RL_points[1]] += math.ceil(lenRL/2)
print(*res)