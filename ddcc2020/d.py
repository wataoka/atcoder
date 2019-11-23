M = int(input())
d, c = [], []
N = ''
for i in range(M):
    di, ci = map(int, input().split())
    N += str(di)*ci
N = list(N)

num_round = 0
while True:
    if int(''.join(N)) <= 9:
        break
    n_list = []
    max_n = 0
    max_i = 0
    for i in range(len(N)-1):
        n = int(''.join(N[:i])+str(int(N[i])+int(N[i+1]))+''.join(N[i+2:]))
        if max_n < n:
            max_n = n
            max_i = i
    N = list(str(max_n))
    num_round += 1
print(num_round)