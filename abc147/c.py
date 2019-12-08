import itertools
from collections import defaultdict

def ok_bit(bit):
    for i in range(N):
        if bit[i] == 0:
            continue
        for x, y in evidence_dict[i]:
            if y != bit[x-1]:
                return False
    return True



def solver():
    for bit in reversed(bit_list):
        if ok_bit(bit):
            return bit
    return [0]

N = int(input())
evidence_dict = defaultdict(list)
A = []
for i in range(N):
    A1 = int(input())
    for j in range(A1):
        evidence_dict[i].append(list(map(int, input().split())))

L = [0, 1]
bit_list = list(itertools.product(L, repeat=N))


if __name__ == "__main__":
    ans_bit = solver()
    res = 0
    for b in ans_bit:
        if b==1:
            res+=1
    print(res)