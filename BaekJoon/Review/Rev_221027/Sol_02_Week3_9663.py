"""
https://www.acmicpc.net/problem/9663
"""


def diagonal_validation(B, col, val):
    for i in range(len(B)):
        if i != col and B[i] is not None and val - B[i] == abs(i - col):
            # print('diagonal_validation, B[i] : {}, val : {}, i : {}, col : {}'.format(B[i], val, i, col))
            return False

    return True


def recursively_put_queen(B, cnt=0):
    if cnt == len(B):
        return True, 1

    result = 0
    for i in range(len(B)):
        if B[i] is None and diagonal_validation(B, i, cnt):
            B[i] = cnt
            go_on, result_cnt = recursively_put_queen(B, cnt+1)
            if go_on:
                result += result_cnt
            B[i] = None

    if result > 0:
        return True, result
    else:
        return False, result


if __name__ == '__main__':
    N = int(input())
    board = [None] * N

    finale, result = recursively_put_queen(board)
    print(result)
