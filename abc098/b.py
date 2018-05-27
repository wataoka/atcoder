import sys

N = int(input())
S = input()

max = -1

for i in range(1, N):
    X = S[:i]
    Y = S[i:]

    cnt = 0
    for j in X:
        for k in Y:
            if j==k:
                cnt += 1
                break
    if cnt > max:
        max = cnt

print(max)
