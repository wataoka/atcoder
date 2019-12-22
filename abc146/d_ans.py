from collections import defaultdict, deque

N = int(input())
E = [[] for _ in range(N+1)]
edge_order = []
for i in range(N-1):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)
    edge_order.append(b)


# node: (id, parent_id)
root_node = (1, -1)
open_list = deque([root_node])
ans = {}
colors = [-1]*(N+1)
while open_list:
    cur_node = open_list.popleft()
    cur_id, parent_id = cur_node
    adj_id_list = E[cur_id]
    c = 1
    for child_id in adj_id_list:
        if child_id == parent_id:
            continue
        if c == colors[cur_id]:
            c += 1
        colors[child_id] = c
        c += 1
        open_list.append((child_id, cur_id))

print(max(colors))
for i in edge_order:
    print(colors[i])