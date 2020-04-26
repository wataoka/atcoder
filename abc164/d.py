S = input()
N = len(S)

ans = 0
i = 0; j = 4
while True:

    if i >= N-3 or len(S) <= 4:
        break
    if j >= N:
        i += 1
        j = i+4

    print(i, j, S, ans)
    target = int(S[i:j])

    if target%2019==0:
        ans += 1
        S = S[:i+1]+S[j+1:]
    else:
        j+=1
print(ans)