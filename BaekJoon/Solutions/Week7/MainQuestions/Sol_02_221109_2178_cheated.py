"""
https://www.acmicpc.net/problem/2178
"""


def dfs(N, M, L, x, y, path=None, min_depth=None):
    if path is None:
        path = set()

    if min_depth is not None:
        if len(path) + 1 >= min_depth:
            return False, None
        if min_depth - len(path) < (N-x) + (M-y):
            return False, None
        if min_depth <= N+M:
            return False, None

    if x == N-1 and y == M-1:
        result = len(path) + 1
        if min_depth is not None and min_depth <= result:
            return False, None
        else:
            return True, result

    path.add((x, y))
    # print('min_depth : {}, path : {}'.format(min_depth, path))
    if x < N-1 and L[x+1][y] == '1' and (x+1, y) not in path:
        go_on, temp = dfs(N, M, L, x+1, y, path, min_depth)
        if go_on:
            min_depth = min(min_depth, temp) if min_depth is not None else temp
    if y < M-1 and L[x][y+1] == '1' and (x, y+1) not in path:
        go_on, temp = dfs(N, M, L, x, y+1, path, min_depth)
        if go_on:
            min_depth = min(min_depth, temp) if min_depth is not None else temp
    if x > 0 and L[x-1][y] == '1' and (x-1, y) not in path:
        go_on, temp = dfs(N, M, L, x-1, y, path, min_depth)
        if go_on:
            min_depth = min(min_depth, temp) if min_depth is not None else temp
    if y > 0 and L[x][y-1] == '1' and (x, y-1) not in path:
        go_on, temp = dfs(N, M, L, x, y-1, path, min_depth)
        if go_on:
            min_depth = min(min_depth, temp) if min_depth is not None else temp

    path.remove((x, y))

    if min_depth is not None:
        return True, min_depth
    else:
        return False, None


def get_coordinate(N, M, num):
    return num % M, num // M


def get_idx(N, M, x, y):
    return x + y*M


from collections import deque
def bfs(N, M, L):
    record = [None] * (N*M)
    record[0] = 1
    Q = deque()
    Q.append(0)
    while len(Q) > 0:
        popped = Q.popleft()
        x, y = get_coordinate(N, M, popped)

        if x < M-1 and L[y][x+1] == '1':
            target = get_idx(N, M, x+1, y)
            if (record[target] is None) or (record[target] > record[popped]+1):
                record[target] = record[popped]+1
                Q.append(target)

        if y < N-1 and L[y+1][x] == '1':
            target = get_idx(N, M, x, y+1)
            if (record[target] is None) or (record[target] > record[popped]+1):
                record[target] = record[popped]+1
                Q.append(target)

        if x > 0 and L[y][x-1] == '1':
            target = get_idx(N, M, x-1, y)
            if (record[target] is None) or (record[target] > record[popped]+1):
                record[target] = record[popped]+1
                Q.append(target)

        if y > 0 and L[y-1][x] == '1':
            target = get_idx(N, M, x, y-1)
            if (record[target] is None) or (record[target] > record[popped]+1):
                record[target] = record[popped]+1
                Q.append(target)

        # print(record)
    return record[-1]



if __name__ == '__main__':
    N, M = map(int, input().split())
    labyrinth = [input() for _ in range(N)]

    # # N, M = 100, 100
    # # line = ['1' for _ in range(100)]
    # # labyrinth = [''.join(line) for _ in range(N)]
    # #
    # # print(labyrinth)
    #
    # finale, result = dfs(N, M, labyrinth, 0, 0)
    # print(result)

    # for i in range(25):
    #     coord = get_coordinate(5, 5, i)
    #     print(coord)
    #     print(get_idx(5, 5, coord[0], coord[1]))

    result = bfs(N, M, labyrinth)
    print(result)
