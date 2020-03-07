n, a, b = map(int, input().split(' '))

if a==0:
    print(0)
    exit(0)

ans = 0

num_br = n//(a+b)

if num_br == 0:
    if n >= a:
        print(a)
        exit(0)
    else:
        print(n)
        exit(0)

ans += (num_br)*a
ans += min(a, n - num_br*(a+b))

print(ans)