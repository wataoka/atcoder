n, m = map(int, input().split())
flags = [False]*n
num_ac = 0
num_wa = 0
wa_list = [0]*n

for i in range(m):
    p, s = input().split()
    p = int(p)
    if flags[p-1]:
        continue
    else:
        if s=='WA':
            wa_list[p-1] += 1
        else:
            flags[p-1] = True
            num_ac += 1
            num_wa += wa_list[p-1]

print(num_ac, num_wa)