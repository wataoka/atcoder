N, K = map(int, input().split())

all_sunuke = list(range(1, N+1))

have_sunuke = []

for i in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    have_sunuke += A

print(len(list(set(all_sunuke)-set(have_sunuke))))