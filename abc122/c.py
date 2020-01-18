N, Q = map(int, input().split())
S = list(input())

# cum[i]: S[0]~S[i]におけるACの数
cum = [0]
cnt = 0
for i in range(1, N):
    if S[i-1]+S[i] == 'AC':
        cnt+=1
    cum.append(cnt)

ans = []
for i in range(Q):
    l, r = map(int, input().split())
    ans.append(cum[r-1] - cum[l-1])

for i in ans:
    print(i)