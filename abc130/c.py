W, H, x, y = list(map(int, input().split()))

S = W*H
if W==2*x and H==2*y:
    print(S/2, 1)
else:
    print(S/2, 0)