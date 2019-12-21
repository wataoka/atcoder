import math

S_list = list(input().split('LR'))
for i in range(len(S_list)):
    if len(S_list) == 1:
        break
    if i==0:
        S_list[i] = S_list[i]+'L'
    elif i==len(S_list)-1:
        S_list[i] = 'R' + S_list[i]
    else:
        S_list[i] = 'R' + S_list[i] + 'L'

ans = []
for S in S_list:
    cnt = [0]*len(S)
    for i in range(len(S)-1):
        if S[i]+S[i+1]=='RL':
            R_idx = i
            L_idx = i+1
            break
    num_odd = math.floor(len(S)/2)
    num_even = math.ceil(len(S)/2)
    if R_idx%2==0:
        cnt[R_idx] = num_even
        cnt[L_idx] = num_odd
    else:
        cnt[R_idx] = num_odd
        cnt[L_idx] = num_even
    ans += cnt
print(*ans)