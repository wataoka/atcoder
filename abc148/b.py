n = int(input())
S, T = input().split()
S = list(S)
T = list(T)
ans = ""
for i in range(n):
    ans += (str(S[i])+str(T[i]))
print(ans)

