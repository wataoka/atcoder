from functools import lru_cache

def pascal(n:int, INF=10**9+7):

    @lru_cache(maxsize=1000)
    def c(n,k): 
      return 1 if(k<=0 or n<=k) else ( c(n-1, k-1) + c(n-1, k) ) % INF

    pascal_list = []
    for i in range(n):
        pascal_list.append([c(i, j) for j in range(i+1)])
    return pascal_list