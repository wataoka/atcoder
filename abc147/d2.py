import numpy as np

N = int(input())
A = list(input().split())
d_to_num1 = {}
max_len = 0
for i in range(N):
    a = list(bin(int(A[i]))[2:])
    if max_len <= len(a):
        max_len = len(a)
    for j,b in enumerate(reversed(a)):
        if b=='1':
            if not(j in d_to_num1.keys()):
                d_to_num1[j]=1
            else:
                d_to_num1[j]+=1 
        
if __name__ == "__main__":

    res = 0
    mod = 10**9+7

    for i in range(max_len):
        if not(i in d_to_num1.keys()):
            num_1 = 0
        else:
            num_1 = d_to_num1[i]
        num_0 = (N-num_1)%mod
        tmp = 1
        tmp *= num_1
        tmp %= mod
        tmp *= num_0
        tmp %= mod
        for _ in range(i):
            tmp = (tmp*2)%mod
        res += tmp%mod
        res %= mod
    print(res)