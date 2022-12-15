"""
2580. 스도쿠
https://www.acmicpc.net/problem/2580
"""
import sys
from copy import deepcopy
from itertools import permutations

sys.setrecursionlimit(100000)

def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()


def recursive_fill_by_row(board, blank_map, cnt=0):
    target_row = None
    for key in blank_map.keys():
        target_row = key
        if target_row is not None:
            break

    if target_row is None:
        return True, board, cnt

    print('In recursive_fill_by_row, row : {}, cnt : {}'.format(target_row, cnt))
    print_board(board)
    print('-----------------------')


    indices = blank_map[target_row]['indices']
    values = blank_map[target_row]['values']
    # print('indices : {}'.format(indices))
    for perm in permutations(values):
        # print('perm : {}'.format(perm))
        c_board = deepcopy(board)
        for k in range(len(indices)):
            c_board[target_row][indices[k]] = perm[k]
            coordinate = (target_row, indices[k])
            go_on = col_validation(c_board, indices[k]) & partition_validation(board, coordinate)
            if not go_on:
                break
        if go_on:
            c_blank_map = deepcopy(blank_map)
            del c_blank_map[target_row]
            go_next, new_board, cnt_delta = recursive_fill_by_row(c_board, c_blank_map, cnt+1)
            cnt += cnt_delta
            if go_next:
                return True, new_board, cnt
    return False, board, cnt


def col_validation(board, col_idx):
    # print('In col_validation, col : {}'.format(col_idx))
    test = [0 for _ in range(9)]
    for i in range(9):
        num = board[i][col_idx]
        if num != 0:
            if test[num-1] != 0:
                # print('Fail : {}'.format(test))
                return False
            else:
                test[num-1] = num
    # print('Success : {}'.format(test))
    return True


def partition_validation(board, coordinate):
    test = [0 for _ in range(9)]
    partition_row_start = coordinate[0]//3
    partition_col_start = coordinate[1]//3
    # print('In partition_validation, coordinate : {}, partition_x_start : {}, partition_y_start : {}'.format(coordinate, partition_row_start, partition_col_start))
    for i in range(3):
        for j in range(3):
            num = board[partition_row_start*3+i][partition_col_start*3+j]
            # print(num)
            if num != 0:
                if test[num-1] != 0:
                    # print('Fail : {}'.format(test))
                    return False
                else:
                    test[num-1] = num
    # print('Success : {}'.format(test))
    return True


if __name__ == '__main__':
    board = [list(map(int, input().split())) for _ in range(9)]

    # print_board(board)

    blank_map_by_row = {}
    for i in range(9):
        test = [0 for _ in range(9)]
        indices = []
        values = []
        for j in range(9):
            if board[i][j] == 0:
                indices.append(j)
            else:
                test[board[i][j]-1] = 1
        for j in range(9):
            if test[j] == 0:
                values.append(j+1)
        blank_map_by_row[i] = {'indices': indices, 'values': values}

    # print(blank_map_by_row)
    finale, board, cnt = recursive_fill_by_row(board, blank_map_by_row)
    if finale:
        print('After {} calculations...'.format(cnt))
        print_board(board)