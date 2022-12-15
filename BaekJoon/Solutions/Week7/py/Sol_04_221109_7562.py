"""
https://www.acmicpc.net/problem/7562
"""
from collections import deque


def knight_availables(I, x, y):
    if x >= 2:
        if y >= 1:
            yield x-2, y-1
        if y < I-1:
            yield x-2, y+1
    if x < I-1-2:
        if y >= 1:
            yield x+2, y-1
        if y < I-1:
            yield x+2, y+1

    if y >= 2:
        if x >= 1:
            yield x-1, y-2
        if x < I-1:
            yield x+1, y-2
    if y < I-1-2:
        if x >= 1:
            yield x-1, y+2
        if x < I-1:
            yield x+1, y+2


def print_board(I, R):
    for i in range(I):
        for j in range(I):
            print(R[i][j], end="") if R[i][j] is not None else print('_', end="")
        print()
    print()


def min_knight_movement(I, K, T):
    record = [[None] * I for _ in range(I)]
    record[K[0]][K[1]] = 0
    Q = deque()
    Q.append(K)
    while len(Q) > 0:
        popped = Q.popleft()
        for position in knight_availables(I, popped[0], popped[1]):
            if record[position[0]][position[1]] is None or record[position[0]][position[1]] > record[popped[0]][popped[1]] + 1:
                record[position[0]][position[1]] = record[popped[0]][popped[1]] + 1

                if position[0] == T[0] and position[1] == T[1]:
                    break

                Q.append(position)
                # print_board(I, record)

    return record[T[0]][T[1]]


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        I = int(input())
        knight = list(map(int, input().split()))
        target = list(map(int, input().split()))
        # print(I, knight, target)
        print(min_knight_movement(I, knight, target))

"""
1
8
0 0
7 0
"""