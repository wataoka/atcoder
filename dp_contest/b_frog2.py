N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [0]*N

for i in range(1, N):
    h_to = h[i]
    dp[i] = min(
        [
            dp_from + abs(h_to - h_from)
            for dp_from, h_from in zip(
                dp[max(0, i-K):i], h[max(0, i-K):i]
            )
        ]
    )