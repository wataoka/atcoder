import math

S = list(input())

S1 = "01"*(len(S)//2)
if len(S1)<len(S):
    S1 += "0"
S2 = "10"*(len(S)//2)
if len(S2)<len(S):
    S2 += "1"

cnt1, cnt2 = 0, 0
for i in range(len(S)):
    if S[i] != S1[i]:
        cnt1 += 1
    if S[i] != S2[i]:
        cnt2 += 1
print(min(cnt1, cnt2))