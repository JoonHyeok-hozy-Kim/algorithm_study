"""
https://www.acmicpc.net/problem/16236
"""
from collections import deque
from copy import deepcopy


def play(B, E, BF, shark_position, shark_size, time_cnt=0, stomach=0):
    if len(E) == 0:
        # print(BF)
        return time_cnt

    meal, moved_distance = find_meal(B, E, shark_position, shark_size)
    # print('meal : {}, moved_distance : {}'.format(meal, moved_distance))
    if meal is None:
        return time_cnt
    E.remove(meal)
    shark_position = meal
    stomach += 1
    if stomach == shark_size:
        stomach = 0
        shark_size += 1
    time_cnt += moved_distance
    # print('meal : {}, moved_distance : {}, shark_size : {}, stomach : {}, time_cnt : {}'.format(meal, moved_distance, shark_size, stomach, time_cnt))
    if shark_size-1 < len(BF) and len(BF[shark_size-1]) > 0:
        E.extend(BF[shark_size-1])
        BF[shark_size-1] = []
    return play(B, E, BF, shark_position, shark_size, time_cnt, stomach)


def find_meal(B, E, shark_position, shark_size):
    candidates = []
    min_distance = None
    for e in E:
        temp_distance = get_distance(B, e, shark_position, shark_size)
        if temp_distance is not None:
            if min_distance is None or temp_distance < min_distance:
                min_distance = temp_distance
                candidates = [e]
            elif min_distance == temp_distance:
                candidates.append(e)

    # print(candidates)
    return get_priority(candidates), min_distance


def get_distance(B, e, shark_position, shark_size):
    N = len(B)
    temp_board = [[None] * N for _ in range(N)]
    temp_board[shark_position[0]][shark_position[1]] = 0
    Q = deque()
    Q.append(shark_position)
    while len(Q) > 0:
        popped = Q.popleft()
        for i in range(4):
            target = [popped[0], popped[1]]
            if i%4 == 0:
                target[0] += 1
            elif i%4 == 1:
                target[0] -= 1
            elif i%4 == 2:
                target[1] += 1
            else:
                target[1] -= 1

            if target[0] == e[0] and target[1] == e[1]:
                return temp_board[popped[0]][popped[1]] + 1
            elif 0 <= target[0] < N and 0 <= target[1] < N and B[target[0]][target[1]] <= shark_size:
                if temp_board[target[0]][target[1]] is None or temp_board[target[0]][target[1]] > temp_board[popped[0]][popped[1]] + 1:
                    temp_board[target[0]][target[1]] = temp_board[popped[0]][popped[1]] + 1
                    Q.append([target[0], target[1]])

            # print(temp_board)


def get_priority(C):
    if len(C) == 0:
        return None
    if len(C) == 1:
        return C[0]
    ordered_vertically = []
    min_y = None
    for v in C:
        if min_y is None or min_y > v[0]:
            min_y = v[0]
            ordered_vertically = [v]
        elif min_y == v[0]:
            ordered_vertically.append(v)
    if len(ordered_vertically) == 1:
        return ordered_vertically[0]
    final = None
    for v in ordered_vertically:
        if final is None or final[1] > v[1]:
            final = v
    return final


if __name__ == '__main__':
    N = int(input())
    shark_position = None
    shark_size = 2
    edibles = []
    big_fish = [[] for i in range(9)]
    board = [None] * N
    for i in range(N):
        temp = [None] * N
        j = 0
        for box in map(int, input().split()):
            temp[j] = box
            if box == 9:
                shark_position = [i, j]
                temp[j] = 0
            elif box > 1:
                big_fish[box].append((i, j))
            elif box > 0:
                edibles.append((i, j))
            j += 1
        board[i] = temp

    # print('board : {}'.format(board))
    # print('edibles : {}'.format(edibles))
    # print('big_fish : {}'.format(big_fish))
    # print('shark_position : {}'.format(shark_position))

    # print(find_meal(board, edibles, shark_position, shark_size))
    result = play(board, edibles, big_fish, shark_position, shark_size)
    print(result)

"""
3
1 0 0
3 3 3
0 9 0
"""