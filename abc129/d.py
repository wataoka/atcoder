H, W = map(int, input().split())
grid = []
for i in range(H):
    grid.append(list(input()))

if __name__ == "__main__":

    U = [[0 for _ in range(W)] for _ in range(H)]
    D = [[0 for _ in range(W)] for _ in range(H)]
    R = [[0 for _ in range(W)] for _ in range(H)]
    L = [[0 for _ in range(W)] for _ in range(H)]
    for col in range(W):
        for row in range(H):
            if grid[row][col] != '#':
                if row == 0:
                    U[row][col] = 1
                else:
                    U[row][col] = U[row-1][col]+1
            if grid[(H-1)-row][col] != '#':
                if (H-1)-row == H-1:
                    D[(H-1)-row][col] = 1
                else:
                    D[(H-1)-row][col] = D[(H-1)-row+1][col]+1
    for row in range(H):
        for col in range(W):
            if grid[row][col] != '#':
                if col == 0:
                    L[row][col] = 1
                else:
                    L[row][col] = L[row][col-1]+1
            if grid[row][(W-1)-col] != '#':
                if (W-1)-col == W-1:
                    R[row][(W-1)-col] = 1
                else:
                    R[row][(W-1)-col] = R[row][(W-1)-col+1]+1
    
    ans = 0
    for row in range(H):
        for col in range(W):
            if grid[row][col] == '#':
                continue
            score = U[row][col]+D[row][col]+L[row][col]+R[row][col]-3
            if ans < score:
                ans = score
    print(ans)