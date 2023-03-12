from collections import deque
from copy import deepcopy

def find_path(grid):
    row_size = len(grid)
    col_size = len(grid[0])
    Q = deque()
    Q.append([(0, 0)])
    while len(Q) > 0:
        popped_route = Q.popleft()
        if len(popped_route) >= row_size - 1 + col_size - 1:
            return popped_route

        last_row, last_col = popped_route[-1][0], popped_route[-1][1]
        if last_row + 1 < row_size and grid[last_row+1][last_col] == 0:
            new_route = deepcopy(popped_route)
            new_route.append((last_row+1, last_col))
            Q.append(new_route)
        if last_col + 1 < col_size and grid[last_row][last_col+1] == 0:
            new_route = deepcopy(popped_route)
            new_route.append((last_row, last_col+1))
            Q.append(new_route)
    

def show_grid(grid):
    for i in grid:
        print("--", end="")
    print()
    for i, iv in enumerate(grid):
        for j, jv in enumerate(iv):
            print(jv, end=" ")
        print()
    for i in grid:
        print("--", end="")
    print()


if __name__ == '__main__':
    row, col = 3, 3
    G = [[0 for i in range(col)] for j in range(row)]
    # show_grid(G)
    G[0][2] = 1
    G[1][1] = 1
    show_grid(G)

    print(find_path(G))