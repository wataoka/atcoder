S = list(input())
T = list(input())

res = 0
for s, t in zip(S, T):
    if s==t:
        res+=1
print(res)