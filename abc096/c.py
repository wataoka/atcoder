import sys

h, w = map(int, input().split())

s = []
for i in range(h):
    s.append(input())

ans = True
flag = False

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            search_list = []
            if i==0:
                if j==0:
                    search_list = [s[i+1][j], s[i][j+1]]
                elif j==w-1:
                    search_list = [s[i+1][j], s[i][j-1]]
                else:
                    search_list = [s[i][j-1], s[i+1][j], s[i][j+1]]

            if i==h-1 and j==0: search_list = [s[i-1][j], s[i][j+1]]
            if i==w-1 and j==w-1: search_list = [s[i-1][j], s[i][j-1]]
            if j==0: search_list = [s[i-1][j], s[i+1][j], s[i][j+1]]
            if i==h-1: search_list = [s[i-1][j], s[i][j-1], s[i][j+1]]
            if j==w-1: search_list = [s[i-1][j], s[i][j-1], s[i+1][j]]

    if not(ans):
        break

if ans:
    print('Yes')
else:
    print('No')
