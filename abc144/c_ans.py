"""
(1, 1)から(a, b)に至るまでの移動回数はa+b-2.
したがって, 問題は「a×b=Nとなるような(a, b)について, a+b-2の最小値を求めよ.」となる.
対称性からa<=bとしてよりので, a<=sqrt(N)までを全探索することによりO(sqrt(N))で解くことができる.
"""

import math

N = int(input())

res = 10**12+1

if N==1:
    print(0)
else:
    for a in range(1, int(math.sqrt(N))+1):
        if (N%a)==0:
            b = int(N/a)
            if res>a+b-2:
                res = a+b-2
    
    if res == 10**12+1:
        print(N-1)
    else:
        print(res)