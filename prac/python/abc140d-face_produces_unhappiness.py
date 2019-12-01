N, K = map(int, input().split())
S = list(input())

# 向かい合ってるor背を向けてる場所を検知
num_diff = 0
pre_s = S[0]
for cur_s in S[1:]:
    if pre_s != cur_s:
        num_diff += 1
    pre_s = cur_s

for i in range(K):
    if num_diff <= 1:
        num_diff = 0
        break
    num_diff -= 2

print(N-1-num_diff)