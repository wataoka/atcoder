def remaining(s1, s2):
    if not('R' in [s1, s2]):
        return 'R'
    elif not('G' in [s1, s2]):
        return 'G'
    else:
        return 'B'

N = int(input())
S = list(input())

# acc[color][i]: i番目からN番目までのcolorの数
acc = {
    'R': [0 for _ in range(N)],
    'G': [0 for _ in range(N)],
    'B': [0 for _ in range(N)]
}
acc[S[-1]][-1] = 1
for i in range(N-2, -1, -1):
    acc[S[i]][i] = acc[S[i]][i+1]+1
    if S[i] == 'R':
        acc['G'][i] = acc['G'][i+1]
        acc['B'][i] = acc['B'][i+1]
    elif S[i] == 'G':
        acc['R'][i] = acc['R'][i+1]
        acc['B'][i] = acc['B'][i+1]
    else:
        acc['G'][i] = acc['G'][i+1]
        acc['R'][i] = acc['R'][i+1]


if __name__ == "__main__":
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            if S[i]==S[j]:
                continue
            color = remaining(S[i], S[j])
            ans += acc[color][j+1]
            if j+j-i < N:
                if S[j+(j-i)] != S[i] and S[j+(j-i)] != S[j]:
                    ans -= 1
    print(ans)