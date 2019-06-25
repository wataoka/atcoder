import sys

A, B, T = map(int, input().split())

i = 0
while True:
    if (i*A > T+0.5):
        break
    else:
        i += 1

print(B*(i-1))