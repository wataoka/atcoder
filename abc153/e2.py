from math import ceil
H, N = map(int, input().split())
A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

# dp[i]: 体力をi以下にできる最小mp消費量
dp = [float('inf') for _ in range(H+1)]
dp[H] = 0
for i in range(N):
    a, b = A[i], B[i]
    num_attack = int(ceil(H//a))
    tmp_H = H
    for j in range(1, num_attack):
        tmp_H = H-(j*a)
        for k in range(tmp_H, tmp_H+a):
            if k+a >= H+1:
                continue
            dp[k] = min(dp[k], dp[k+a]+b)
    # ラスト
    for k in range(0, tmp_H):
        if k+a >= H+1:
            continue
        dp[k] = min(dp[k], dp[k+a]+b)
    
    print(*dp)