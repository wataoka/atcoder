N = int(input())
S = list(input())

ans = 0
for i in range(N-2):
    if S[i] + S[i+1] + S[i+2] == 'ABC':
        ans += 1
print(ans)
