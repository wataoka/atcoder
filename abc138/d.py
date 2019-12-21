from collections import defaultdict

N, Q = map(int, input().split())
edge = defaultdict(list)
for i in range(N-1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

cnt = [0]*(N+1)
for i in range(Q):
    p, x = map(int, input().split())
    cnt[p] += x

root_node = (1, -1) # (id, parent_id)
open_list = [root_node]
closed_list = []
while True:
    if len(open_list) == 0:
        break
    cur_node = open_list.pop()
    cur_id, parent_id = cur_node
    if not(parent_id == -1):
        cnt[cur_id] += cnt[parent_id]
    for child_id in edge[cur_id]:
        if child_id == parent_id:
            continue
        open_list.append((child_id, cur_id))
print(*cnt[1:])