import sys
from collections import deque

def input():
    return sys.stdin.readline()[:-1]

def solve():
    N, P = map(int, input().split())
    S = input()
    if 10%P == 0:
        ans = 0
        for i in range(N):
            if int(S[N-i-1]) % P == 0:
                ans += N - i
        
        return ans
    
    ten = 1
    cur = 0
    val = [0] * P
    val[cur] += 1
    for i in range(N):
        cur = (cur + int(S[N-i-1])*ten) % P
        ten *= 10
        ten %= P
        val[cur] += 1
    ans = 0
    for p in range(P):
        ans += val[p] * (val[p] - 1) // 2
    
    return ans

if __name__ == "__main__":
    print(solve())