def sum_range(a, b):
    a -= 1
    sum_a = a*(a+1)//2
    sum_b = b*(b+1)//2
    return sum_b - sum_a

N, K = map(int, input().split())

all_sum = sum_range(1, N) - sum_range(1, K-1)+1
print(all_sum)

for i in range(0, N+1-K-1):
    if sum_range(N-(K+i), N) - sum_range(0, K+i) < 0:
        continue
    all_sum +=  sum_range(N-(K+i), N) - sum_range(0, K+i)

print(all_sum+1)