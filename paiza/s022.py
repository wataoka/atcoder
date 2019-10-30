import math
import numpy as np


L, D = map(int, input().split())
N = int(input())
x, y, r = [], [], []
for i in range(N):
    x_i, y_i, r_i = map(int, input().split())
    x.append(x_i)
    y.append(y_i)
    r.append(r_i)

def distance(x1, y1, x2, y2):
    return math.sqrt(
        (abs(x1 - x2))**2 + (abs(y1 - y2))**2
    )

def i2y(col):
    return D - col


if __name__ == "__main__":

    field = [[[0]*N for i in range(L+1)] for j in range(2*D+1)]
    
    for i in range(2*D+1):
        for j in range(L+1):
            for k in range(N):
                d = distance(j, i2y(i), x[k], y[k])
                if r_i >= d:
                    field[i][j][k] = 1
    
    censors = []
    for j in range(L+1):
        col_slice = [row[j] for row in field]
        if all(list(map(lambda x: 1 in x, col_slice))):
            censors.append([0]*N)
            for i in col_slice:
                for k in censors[-1]:
                    if i[k] == 1:
                        censors[-1][k] = 1

    res = 0
    while True:

        if censors == []:
            break

        count_censors = [0]*N
        for k in range(N):
            count_censors[k] = sum([censor[k] for censor in censors])
        max_idx = count_censors.index(max(count_censors))

        for i, c in enumerate(censors):
            if c[max_idx] == 1:
                del censors[i]

        res += 1

    print(res)