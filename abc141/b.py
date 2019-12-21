S = list(input())
for i, s in enumerate(S):
    if (i+1)%2==1:
        if s=='L':
            print('No')
            exit(0)
    if (i+1)%2==0:
        if s=='R':
            print('No')
            exit(0)
print('Yes')