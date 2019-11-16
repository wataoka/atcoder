# reference to https://qiita.com/masashi127/items/0c794e28f4b295ad82c6

"""
A*アルゴリズム
"""

import heapq
import itertools
import numpy as np

# targetの座標を返す関数
def find_pos(pos, maze):
    for i, l in enumerate(maze):
        for j, c in enumerate(l):
            if c == pos:
                return (i, j)

# posから探索可能な四方の座標リストを返す関数
def nexts(pos, maze, wall="#"):
    for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        if maze[pos[0]+a][pos[1]+b] != wall:
            yield (pos[0]+a, pos[1]+b)

# 予測評価関数
def heuristic(pos, goal):
    return max(abs(pos[0]-goal[0]), abs(pos[1]-goal[1]))

# 累積コスト関数
def cumulative_cost(path):
    return len(path)

# 迷路をレンダリングする関数
def render_path(path, maze):
    buf = [[ch for ch in l] for l in maze]
    for pos in path[1:-1]:
        buf[pos[0]][pos[1]] = "o"
    buf[path[0][0]][path[0][1]] = "s"
    buf[path[-1][0]][path[-1][1]] = "g"
    return ["".join(l) for l in buf]


# A*アルゴリズム
def astar(start_pos, goal_pos, maze):
    start_score = 0 + heuristic(start_pos, goal_pos)

    open_list = []
    heapq.heappush(open_list, (start_score, [start_pos]))
    score_dict = {start_pos: start_score}

    while len(open_list) > 0:
        _, closed_list = heapq.heappop(open_list)
        last_closed_pos = closed_list[-1]

        if last_closed_pos == goal:
            return closed_list
        
        for cur_pos in nexts(last_closed_pos, maze):
            cur_pos_score = cumulative_cost(closed_list+[cur_pos]) + heuristic(cur_pos, goal_pos)
            if not(cur_pos in score_dict) or cur_pos_score < score_dict[cur_pos]:
                score_dict[cur_pos] = cur_pos_score
                heapq.heappush(open_list, (cur_pos_score, closed_list+[cur_pos]))

    return []

if __name__ == "__main__":

    maze = [
        "g...#####",
        ".....#.##",
        "##..#####",
        "#......##",
        "#......##",
        "#......##",
        "#...#...#",
        "#.......#",
        "#.....s.#"
        ]
    
    maze = list(map(lambda x: list(x), maze))
    maze = np.pad(maze, 1, 'constant', constant_values='#').tolist()

    start = find_pos("s", maze)
    goal = find_pos("g", maze)


    path = astar(start, goal, maze)

    if len(path) > 0:
        print("\n".join(render_path(path, maze)))

    else:
        print('failed')