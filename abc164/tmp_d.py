print('1' * 200000)
quit()

S = input()
N = len(S)

ans = 0
for i in range(N-3):
    for j in range(i+4, N+1):
        if int(S[i:j])%2019==0:
            ans+=1
            break
print(ans)