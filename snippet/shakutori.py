"""
a1, a2, ..., aNの連続部分列の和がK以上である個数を数えた尺取法の例
"""

N, K = map(int, input().split())
A = list(map(int, input().split()))

cum = [0]*N
cum[0] = A[0]
for i in range(1, N):
    cum[i] = cum[i-1]+A[i]

def get_sum_lr(l, r):
    if l==0:
        return cum[r]
    else:
        return cum[r] - cum[l-1]

if __name__ == "__main__":
    r = 0
    res = 0
    for l in range(N):
        while True:
            sum_lr = get_sum_lr(l, r)
            if sum_lr >= K:
                res += N-r
                break
            if r == N-1:
                break
            r += 1
    print(res)