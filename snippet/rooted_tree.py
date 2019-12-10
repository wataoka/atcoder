"""
この例では, 根からの距離をdistanceに記録して行っている.
ほぼ全てにおいてidをそのまま使用しているが, 
distanceのみdistance[id-1]と使用する.
(別にdictで改良してもいい)
"""

from collections import defaultdict

N = int(input())
edge = defaultdict(list)
# 辺の情報と距離を記録
for i in range(N-1):
    u, v, w = map(int, input().split())
    edge[u].append((v, w))
    edge[v].append((u, w))

# 幅優先探索
distance = [0]*N
queue = [(1, -1)]
while True:
    if len(queue) == 0:
        break
    cur_id, parent_id = queue.pop()
    for child_id, w in edge[cur_id].copy():
        if child_id == parent_id:
            continue
        queue.append((child_id, cur_id))
        distance[child_id-1] = distance[cur_id-1] + w