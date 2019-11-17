# posから探索可能なpos listを返却
def search(pos):
    ok_pos = []
    if (pos[0]+1 < x+1) and (pos[1]+2<y+1):
        ok_pos.append((pos[0]+1, pos[1]+2))
    if (pos[0]+2 < x+1) and (pos[1]+1<y+1):
        ok_pos.append((pos[0]+2, pos[1]+1))
    return ok_pos

x, y = map(int, input().split())

grid = [[0 for j in range(x+1)] for i in range(y+1)]

open_list = search((0, 0))

i = 0
while len(open_list) > i:
    cur_pos = open_list[i]
    grid[cur_pos[0]][cur_pos[1]] += 1
    ok_list = search(cur_pos)
    for ok in ok_list:
        open_list.append(ok)
    i += 1

print(grid[-1][-1])