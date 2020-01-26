H = int(input())
num_m = 1
ans = 0
while True:
    if H<2:
        break
    H = H//2
    ans += num_m
    num_m *= 2
print(ans+num_m)