"""
2580. 스도쿠
https://www.acmicpc.net/problem/2580
"""
import sys
from copy import deepcopy
sys.setrecursionlimit(100000)
TESTER = [0] * 9

def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()


def find_by_row(board, blank_map_by_row):
    blank_map_by_col = {}
    L = [i for i in range(9)] if blank_map_by_row is None else blank_map_by_row.keys()

    for i in L:
        temp_blank_list = []
        tester = deepcopy(TESTER)

        for j in range(9):
            if board[i][j] == 0:
                temp_blank_list.append([(i, j)])
            else:
                tester[board[i][j]-1] = 1

        candidates = []
        for k in range(9):
            if tester[k] == 0:
                candidates.append(k+1)

        if len(candidates) == len(temp_blank_list) == 1:
            popped = temp_blank_list.pop()
            board[i][popped[0][1]] = candidates.pop()
        else:
            for blank in temp_blank_list:
                col = blank[0][1]
                if col not in blank_map_by_col:
                    blank_map_by_col[col] = []
                blank.append(deepcopy(candidates))
                blank_map_by_col[col].append(blank)

    return compare_maps(board, blank_map_by_col, blank_map_by_row, 'c', 'r')
    # return board, blank_map_by_col


def find_by_col(board, blank_map_by_col):
    blank_map_by_partition = {}
    for col in blank_map_by_col.keys():
        temp_blank_list = []
        tester = deepcopy(TESTER)
        for row in range(9):
            if board[row][col] == 0:
                temp_blank_list.append([(row, col)])
            else:
                tester[board[row][col]-1] = 1

        candidates = []
        for k in range(9):
            if tester[k] == 0:
                candidates.append(k+1)

        if len(candidates) == len(temp_blank_list) == 1:
            popped = temp_blank_list.pop()
            board[popped[0][0]][col] = candidates.pop()
        else:
            for blank in temp_blank_list:
                partition = (blank[0][0]//3, blank[0][1]//3)
                if partition not in blank_map_by_partition:
                    blank_map_by_partition[partition] = []
                blank.append(deepcopy(candidates))
                blank_map_by_partition[partition].append(blank)

    return compare_maps(board, blank_map_by_partition, blank_map_by_col, 'p', 'c')
    # return board, blank_map_by_partition


def find_by_partition(board, blank_map_by_partition):
    blank_map_by_row = {}
    for partition in blank_map_by_partition.keys():
        temp_blank_list = []
        tester = deepcopy(TESTER)
        # print(partition)
        for i in range(9):
            row, col = partition[0] * 3 + i // 3, partition[1] * 3 + i % 3
            # print(board[row][col])
            if board[row][col] == 0:
                temp_blank_list.append([(row, col)])
            else:
                tester[board[row][col]-1] = 1
        # print('--------------------------')

        candidates = []
        for k in range(9):
            if tester[k] == 0:
                candidates.append(k+1)

        if len(candidates) == len(temp_blank_list) == 1:
            popped = temp_blank_list.pop()
            board[popped[0][0]][popped[0][1]] = candidates.pop()
            # print('{} = {}'.format(popped, board[popped[0][0]][popped[0][1]]))
        else:
            for blank in temp_blank_list:
                row = blank[0][0]
                if row not in blank_map_by_row:
                    blank_map_by_row[row] = []
                blank.append(deepcopy(candidates))
                blank_map_by_row[row].append(blank)

    return compare_maps(board, blank_map_by_row, blank_map_by_partition, 'r', 'p')
    # return board, blank_map_by_row


def recursive_call(board, blank_map=None, cnt=0):
    if blank_map is not None and len(blank_map) == 0:
        print_board(board)
        return

    if cnt%3 == 0:
        board, blank_map = find_by_row(board, blank_map)
    elif cnt%3 == 1:
        board, blank_map = find_by_col(board, blank_map)
    else:
        board, blank_map = find_by_partition(board, blank_map)

    return recursive_call(board, blank_map, cnt+1)


def compare_maps(board, curr_map, prev_map=None, curr_key=None, prev_key=None):
    # print('curr_map : {}'.format(curr_map))
    if prev_map is None or curr_key is None or prev_key is None:
        return board, curr_map

    if curr_key == 'r' and prev_key == 'p':
        for partition in prev_map.keys():
            for e in prev_map[partition]:
                point = e[0]
                candidates = e[1]
                possible = []
                if point[0] in curr_map:
                    for f in range(len(curr_map[point[0]])):
                        if curr_map[point[0]][f][0] == point:
                            for cand1 in candidates:
                                for cand2 in curr_map[point[0]][f][1]:
                                    if cand1 == cand2:
                                        possible.append((f, cand1))
                    if len(possible) == 1:
                        curr_map[point[0]].pop(possible[0][0])
                        board[point[0]][point[1]] = possible[0][1]

    elif curr_key == 'c' and prev_key == 'r':
        for row in prev_map.keys():
            for e in prev_map[row]:
                point = e[0]
                candidates = e[1]
                possible = []
                if point[1] in curr_map:
                    for f in range(len(curr_map[point[1]])):
                        if curr_map[point[1]][f][0] == point:
                            for cand1 in candidates:
                                for cand2 in curr_map[point[1]][f][1]:
                                    if cand1 == cand2:
                                        possible.append((f, cand1))
                    if len(possible) == 1:
                        curr_map[point[1]].pop(possible[0][0])
                        board[point[0]][point[1]] = possible[0][1]
                        # print('board[{}][{}] -> {}'.format(point[0], point[1], possible[0][1]))

    elif curr_key == 'p' and prev_key == 'c':
        for col in prev_map.keys():
            for e in prev_map[col]:
                point = e[0]
                candidates = e[1]
                possible = []
                partition = (e[0][0]//3, e[0][1]//3)
                if partition in curr_map:
                    # print('partition : {}'.format(partition))
                    for f in range(len(curr_map[partition])):
                        if curr_map[partition][f][0] == point:
                            # print('point : {}'.format(point))
                            for cand1 in candidates:
                                for cand2 in curr_map[partition][f][1]:
                                    if cand1 == cand2:
                                        possible.append((f, cand1))
                    if len(possible) == 1:
                        curr_map[partition].pop(possible[0][0])
                        if len(curr_map[partition]) == 0:
                            del curr_map[partition]
                        board[point[0]][point[1]] = possible[0][1]
                        # print('board[{}][{}] -> {}'.format(point[0], point[1], possible[0][1]))

    return board, curr_map



if __name__ == '__main__':
    board = [list(map(int, input().split())) for _ in range(9)]
    blank_map = None
    cnt = 0
    while blank_map is None or len(blank_map) > 0:
        # print(cnt, blank_map, board)
        prev_board = deepcopy(board)
        if cnt%3 == 0:
            board, blank_map = find_by_row(board, blank_map)
        elif cnt%3 == 1:
            board, blank_map = find_by_col(board, blank_map)
        else:
            board, blank_map = find_by_partition(board, blank_map)
        cnt += 1
        if board != prev_board:
            print('-------------------')
            print_board(board)

    print_board(board)
