N = int(input())
X = list(map(int, input().split()))

min_P = 0
min_cost = float('inf')
for P in range(1, 101):
    cost = 0
    for Xi in X:
        cost += (Xi-P)**2
    if min_cost > cost:
        min_cost = cost
        min_P = P
print(min_cost)