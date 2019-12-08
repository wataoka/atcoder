p, q, r = map(int, input().split())
res = p+q+r
res -= max(p, q, r)
print(res)