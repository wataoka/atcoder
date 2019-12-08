import numpy as np

def preprocess(x):
    x = int(x)
    x = bin(x)[2:]
    return x
def preprocess2(x):
    x = x.zfill(max_len)
    x = list(x)
    x = list(map(int, x))
    return x

N = int(input())
A = list(map(preprocess, input().split()))
max_len = max(list(map(lambda b:len(b), A)))
A = list(map(preprocess2, A))
A = np.array(A).T.tolist()


if __name__ == "__main__":
    res = 0
    mod = 10**9+7
    for i, col in enumerate(reversed(A)):
        col = np.array(col)
        num_1 = np.count_nonzero(col)
        num_0 = len(col)-num_1

        tmp = 1
        tmp = tmp*num_0%mod
        tmp = tmp*num_1%mod
        for _ in range(i):
            tmp = tmp*2%mod
        
        res = (res+tmp)%mod
    
    print(res)