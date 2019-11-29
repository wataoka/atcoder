from collections import defaultdict, deque

def get_color(id1, id2):
    return edge_colors_dict[(min(id1, id2), max(id1, id2))]

def set_color(color, id1, id2):
    node_list[id1-1].adj_color_dict[id2] = color
    node_list[id2-1].adj_color_dict[id1] = color
    edge_colors_dict[(min(id1, id2), max(id1, id2))] = color

class Node:

    def __init__(self, id, adj_id_list, adj_color_dict):
        self.id = id
        self.adj_id_list = adj_id_list
        self.adj_color_dict = adj_color_dict
    
    def get_min_color(self):
        exist_colors = []
        for color in self.adj_color_dict.values():
            if color != -1:
                exist_colors.append(color)
        color = 1
        while True:
            if not(color in exist_colors):
                return color
            else:
                color += 1

N = int(input())
adj_dict = defaultdict(list)
edge_colors_dict = {}
a, b = [], []
for i in range(N-1):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
    adj_dict[ai].append(bi)
    adj_dict[bi].append(ai)
    edge_colors_dict[(ai, bi)] = -1

# node_list[id-1]で, idのnodeにアクセス可能.
node_list = []
for id in range(1, N+1):
    adj_id_list = adj_dict[id]
    adj_color_dict = {}
    for adj_id in adj_id_list:
        adj_color_dict[adj_id] = -1
    node = Node(id, adj_id_list, adj_color_dict)
    node_list.append(node)

open_list = deque()
open_list.append(1)
while True:
    if len(open_list) == 0:
        break
    cur_id = open_list.pop()
    cur_node = node_list[cur_id-1]
    for adj_id in cur_node.adj_id_list:
        if get_color(cur_id, adj_id) == -1:
            open_list.append(adj_id)
            new_color = cur_node.get_min_color()
            set_color(new_color, cur_id, adj_id)

print(len(set(edge_colors_dict.values())))
for (ai, bi) in zip(a, b):
    print(edge_colors_dict[(ai, bi)])