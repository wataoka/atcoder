S = input()
cnt = 0
ans = -1
for s in S:
    if s in ['A', 'C', 'G', 'T']:
        cnt += 1
    else:
        if ans < cnt:
            ans = cnt
        cnt = 0
print(max(ans, cnt))
