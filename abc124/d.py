N, K = map(int, input().split())
S = list(input())

# change points
cp = []
pre_s = S[0]
for i, s in enumerate(S[1:]):
    if pre_s != s:
        cp.append(i+1)
        pre_s = s

for p in cp[1:-1]:
    if S[p] == '0':
        num_c = max(2*K, len(cp)-1)
    else:
        num_c = max(2*K+1, len(cp)-1)
    print(cp[num_c]-p)