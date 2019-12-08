N = int(input())
W = list(map(int, input().split()))

abs_diffs = []
for T in range(N-1):
    S1 = sum(W[:T+1])
    S2 = sum(W[T+1:])

    abs_diffs.append(abs(S1-S2))

print(min(abs_diffs))