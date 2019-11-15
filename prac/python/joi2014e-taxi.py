import sys
from collections import deque
from heapq import heappush, heappop

def bfs(s):
    dist = [-1]*N
    dist[s] = 0
    q = deque([])
    q.append(s)

    while q:
        cur_n = q.popleft()
        for near_n in adj_list[cur_n]:
            if dist[near_n] == -1:
                dist[near_n] = dist[cur_n]+1
                if dist[near_n] <= R[s]:
                    adj_list2[s].append((near_n, C[s]))
                q.append(near_n)

def dijkstra():
    dist = [10**18]*N
    dist[0] = 0
    pq = []
    heappush(pq, (dist[0], 0))

    while pq:
        d, cur_n = heappop(pq)
        if dist[cur_n] < d:
            continue

        for near_n, w in adj_list2[cur_n]:
            if dist[near_n] > dist[cur_n]+w:
                dist[near_n] = dist[cur_n]+w
                heappush(pq, (dist[near_n], near_n))
    return dist



N, K = map(int, input().split())
C, R = [], []
for i in range(N):
    ci, ri = map(int, input().split())
    C.append(ci)
    R.append(ri)

adj_list = [[] for _ in range(N)]
for _ in range(K):
    ai, bi = map(int, input().split())
    adj_list[ai-1].append(bi-1)
    adj_list[bi-1].append(ai-1)

adj_list2 = [[] for _ in range(N)]

for i in range(N):
    bfs(i)

print(dijkstra())