"""
根つき木

根つき木について解説している
↓
https://twitter.com/MrWatako/status/1208379759744307201
"""

from collections import defaultdict

N = int(input())

# 隣接するノードの管理(双方向)
edge = defaultdict(list)
for i in range(N-1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

# node: (id, parent_id)
root_node = (1, -1)
open_list = [root_node]
closed_list = []
while True:
    if len(open_list) == 0:
        break
    cur_node = open_list.pop()
    cur_id, parent_id = cur_node
    #
    # 何かしらの処理
    # (例)
    # if not(parent_id == -1):
    #     cur_idとparent_idの重みとか価値の計算的な何か
    #
    for child_id in edge[cur_id]:
        if child_id == parent_id:
            continue
        open_list.append((child_id, cur_id))