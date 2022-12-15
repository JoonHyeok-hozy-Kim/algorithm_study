"""
https://www.acmicpc.net/problem/7569
"""
from collections import deque


def adjacent_tomatoes(M, N, H, t):
    if t[0] > 0:
        yield t[0]-1, t[1], t[2]
    if t[0] < H-1:
        yield t[0]+1, t[1], t[2]
    if t[1] > 0:
        yield t[0], t[1]-1, t[2]
    if t[1] < N-1:
        yield t[0], t[1]+1, t[2]
    if t[2] > 0:
        yield t[0], t[1], t[2]-1
    if t[2] < M-1:
        yield t[0], t[1], t[2]+1


def validate(M, N, H, P, E):
    for empty_space in E:
        for near_empty in adjacent_tomatoes(M, N, H, empty_space):
            if P[near_empty[0]][near_empty[1]][near_empty[2]] == 0:
                return False
    return True


def validate_all(P):
    for i in range(len(P)):
        for j in range(len(P[i])):
            for k in range(len(P[i][j])):
                if P[i][j][k] == 0:
                    return False
    return True


if __name__ == '__main__':
    M, N, H = map(int, input().split())
    pile = [[[None] * M for _ in range(N)] for _ in range(H)]
    initial_ripens = []
    empty_spaces = []
    for i in range(H):
        for j in range(N):
            k = 0
            for x in map(int, input().split()):
                pile[i][j][k] = x
                if x == 1:
                    initial_ripens.append((i, j, k))
                elif x == -1:
                    empty_spaces.append((i, j, k))
                k += 1
    # print(pile)
    # print(initial_ripens)

    Q = deque()
    for ripen in initial_ripens:
        Q.append(ripen)

    max_days = 1
    while len(Q) > 0:
        popped = Q.popleft()
        day_plus_one = pile[popped[0]][popped[1]][popped[2]] + 1
        for not_riped in adjacent_tomatoes(M, N, H, popped):
            if pile[not_riped[0]][not_riped[1]][not_riped[2]] == 0 or pile[not_riped[0]][not_riped[1]][not_riped[2]] > day_plus_one:
                pile[not_riped[0]][not_riped[1]][not_riped[2]] = day_plus_one
                max_days = max(max_days, day_plus_one)
                Q.append(not_riped)
                # print(Q)

    # if validate(M, N, H, pile, empty_spaces):
    #     print(max_days-1)
    if validate_all(pile):
        print(max_days - 1)
    else:
        print(-1)