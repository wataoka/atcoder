N = int(input())
S = []
for _ in range(N):
    s = input()
    S.append(s)
print(len(set(S)))