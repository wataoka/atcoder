from collections import defaultdict, deque

class Node(object):

    def __init__(self, id, person_id=None, children_id=[]):
        self.id = id
        self.person_id = person_id
        self.children_id = children_id
        self.counter = 0


# 標準入力とadj_dictの構築
N, Q = map(int, input().split())

adj_dict = defaultdict(list)
for i in range(N-1):
    ai, bi = map(int, input().split())
    adj_dict[ai].append(bi)
    adj_dict[bi].append(ai)


# グラフの構築
cur_id = 1
cur_node = Node(id=cur_id,
                person_id=None,
                children_id=[])
node_dict = {cur_id:cur_node}
open_list = deque()
open_list.append(cur_id)
while True:
    if len(open_list) == 0:
        break
    cur_id = open_list.pop()
    cur_node = node_dict[cur_id]
    adj_list = adj_dict[cur_id]
    for adj_id in adj_list:
        if adj_id != cur_node.person_id:
            cur_node.children_id.append(adj_id)
            open_list.append(adj_id)
            adj_node = Node(id=adj_id,
                            person_id=cur_id,
                            children_id=[])
            node_dict[adj_id] = adj_node

# 操作jを1つのnodeに対してのみ行う
cur_node = node_dict[1]
p, x = [], []
for i in range(Q):
    pi, xi = map(int, input().split())
    node = node_dict[pi]
    node.counter += xi

# 親ノードから天下り的に加算していく
cur_id = 1
open_list = deque()
open_list.append(cur_id)
while True:
    if len(open_list) == 0:
        break
    cur_id = open_list.pop()
    cur_node = node_dict[cur_id]
    if cur_node.person_id != None:
        cur_node.counter += node_dict[cur_node.person_id].counter
    for child_id in cur_node.children_id:
        open_list.append(child_id)

# 出力
res = []
for id in range(1, N+1):
    res.append(node_dict[id].counter)
print(*res)