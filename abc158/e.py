N, P = map(int, input().split())
S = input()

cnt = 0
Px = 0
while True:
    Px += P
    if Px > int(S):
        break
    if str(Px) in S:
        cnt += S.count(str(Px))
print(cnt)