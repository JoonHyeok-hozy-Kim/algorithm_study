"""
https://www.acmicpc.net/problem/14611
"""
from collections import deque
from heapq import heappop, heappush
from math import inf
X = [-1, 1, 0, 0]
Y = [0, 0, -1, 1]
X8 = [-1, -1, -1, 0, 1, 1, 1, 0]
Y8 = [1, 0, -1, -1, -1, 0, 1, 1]


def exists_invincible_road(N, M, B):
    visited = [[None] * (M+1) for _ in range(N+1)]
    Q = deque()
    Q.append([1, 1])
    while Q:
        i, j = Q.popleft()
        if i == N and j == M:
            return True

        visited[i][j] = 1
        for k in range(4):
            x, y = i+X[k], j+Y[k]
            if 1 <= x <= M and 1 <= y <= N:
                if visited[x][y] is None and B[x][y] == -1:
                    Q.append([x, y])

    return False


def build_walls(N, M, B):
    starting_points = []
    for j in range(2, M+1):
        if B[1][j] != -1:
            starting_points.append((1, j))
    for i in range(2, N):
        if B[i][M] != -1:
            starting_points.append((i, M))
    # print('starting_points : {}'.format(starting_points))

    ending_points = {}
    for i in range(2, N+1):
        if B[i][1] != -1:
            ending_points[(i, 1)] = True
    for j in range(2, M):
        if B[N][j] != -1:
            ending_points[(N, j)] = True

    dp = [[inf] * (M+1) for _ in range(N+1)]
    heap = []
    for sp in starting_points:
        x, y = sp[0], sp[1]
        sp_cost = get_cost_at_position(B, x, y)
        dp[x][y] = sp_cost
        heappush(heap, (sp_cost, (x, y)))

    min_final_cost = None
    while heap:
        popped_cost, (popped_x, popped_y) = heappop(heap)
        if (popped_x, popped_y) in ending_points:
            min_final_cost = min(min_final_cost, popped_cost) if min_final_cost is not None else popped_cost

        for k in range(8):
            x, y = popped_x + X8[k], popped_y + Y8[k]
            if 1 <= x <= N and 1 <= y <= M and B[x][y] != -1:
                added_cost = 0 if B[x][y] == -2 else B[x][y]
                if min_final_cost is None or min_final_cost > popped_cost + added_cost:
                    if popped_cost + added_cost < dp[x][y]:
                        dp[x][y] = popped_cost + added_cost
                        heappush(heap, (popped_cost + added_cost, (x, y)))

    if min_final_cost is None:
        return -1
    else:
        return min_final_cost


def get_cost_at_position(B, i, j):
    if B[i][j] == -2:
        return 0
    elif B[i][j] == -1:
        return None
    else:
        return B[i][j]


if __name__ == '__main__':
    N, M = map(int, input().split())
    board = [[None] * (M+1) for _ in range(N+1)]
    for i in range(1, N+1):
        j = 1
        for k in map(int, input().split()):
            board[i][j] = k
            j += 1
    # print(board)

    # if exists_invincible_road(N, M, board):
    #     print(-1)
    if False:
        print(-1)

    else:
        result = build_walls(N, M, board)
        print(result)


"""
2 2
-1 -1
2 -1


"""