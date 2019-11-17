from functools import lru_cache

INF = 10**9+7

@lru_cache(maxsize=1000)
def c(n,k): 
  return 1 if(k<=0 or n<=k) else ( c(n-1, k-1) + c(n-1, k) ) % INF

for i in range(5):
    print([c(i, j) for j in range(i+1)])

x, y = map(int, input().split())

if (x+y)%3==0:
    k = int((x+y)/3)
    i, j = k, 2*k
    while True:
        if x, y == i, j:
        

else:
    print(0)