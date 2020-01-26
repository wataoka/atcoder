N, K = map(int, input().split())
H = list(map(int, input().split()))
H = sorted(H, reverse=True)
print(sum(H[K:]))