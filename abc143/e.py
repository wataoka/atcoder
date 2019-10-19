def dijkstra(s,n,w,cost):
    #始点sから各頂点への最短距離
    #n:頂点数,　w:辺の数, cost{} : 辺uvのコスト(存在しないときはinf)
    d = [float("inf")] * (n+1)
    used = [False] * (n+1)
    d[s] = 0
    
    while True:
        v = -1
        #まだ使われてない頂点の中から最小の距離のものを探す
        for i in range(n):
            if (not used[i]) and (v == -1):
               v = i
            elif (not used[i]) and d[i] < d[v]:
                v = i
        if v == -1:
               break
        used[v] = True
               
        for j in range(n):
            if (v, j) in cost:
                d[j] = min(d[j],d[v]+cost[(v, j)])
            if (j, v) in cost:
                d[j] = min(d[j],d[v]+cost[(j, v)])
    return d

INF = 10**9 + 1
N, M, L = map(int, input().split())
A, B, C = [], [], []
C = {}
for i in range(M):
    a_i, b_i, c_i = map(int, input().split())
    C[(a_i, b_i)] = c_i

Q = int(input())
for i in range(Q):
    s_i, t_i = map(int, input().split())
    d = dijkstra(s_i, N, M, C)
    print(d)
