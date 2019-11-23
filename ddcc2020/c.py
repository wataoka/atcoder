H, W, K = map(int, input().split())
s = []
for i in range(H):
    s.append(list(input()))

si = 0
paint_h = []
for h in range(H):
    if not('#' in s[h]):
        paint_h.append(h)
        continue
    else:
        for w in range(W):
            if s[h][w] == '#':
                si += 1
                s[h][w] = si
                paint_h.append(h)
                wi = w
                while True:
                    wi += 1
                    if (wi<0)or(wi>=W)or(s[h][wi]!='.'):
                        break
                    s[h][wi] = si
                wi = w
                while True:
                    wi -= 1
                    if (wi<0)or(wi>=W)or(s[h][wi]!='.'):
                        break
                    s[h][wi] = si
        paint_h = []
cnt_non_s = 1
for i in s:
    if '.' in i:
        cnt_non_s += 1
    else:
        tmp = i
        for j in range(cnt_non_s):
            print(*i)
        cnt_non_s = 1

for j in range(cnt_non_s-1):
    print(*tmp)
