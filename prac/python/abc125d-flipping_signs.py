N = int(input())
A = list(map(int, input().split()))

res = 0
min_abs = float('inf')
cnt_neg = 0
for a in A:
    if a < 0:
        cnt_neg += 1
    abs_a = abs(a)
    res += abs_a
    if min_abs > abs_a:
        min_abs = abs_a

if cnt_neg%2==0:
    print(res)
else:
    print(res-2*min_abs)