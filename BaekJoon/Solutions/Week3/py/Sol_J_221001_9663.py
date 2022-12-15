"""
9663. N-Queen
https://www.acmicpc.net/problem/9663
"""
from collections import deque


def _validation(N, Q, new_row, new_col):
    for q_r in range(new_row):
        q_c = Q[q_r]
        if q_c == new_col:
            return False

        right = q_c + (new_row-q_r)
        if N > right == new_col:
            return False
        left = q_c - (new_row-q_r)
        if 0 <= left == new_col:
            return False

    return True


def recursively_get_set(N, Q=None, row=0, cands=None):
    # print('In recursive_check, row : {}, Q : {}'.format(row, Q))
    delta = 0
    if row == 0:
        Q = [None] * N
        cands = deque([n for n in range(N)])

    elif row == N:
        # print(' --> FINAL : {}'.format(Q))
        return 1

    n_cands = len(cands)
    for k in range(n_cands):
        col = cands.popleft()
        if _validation(N, Q, row, col):
            Q[row] = col
            delta += recursively_get_set(N, Q, row+1, cands)
            Q[row] = None
        cands.append(col)

    return delta


if __name__ == '__main__':
    N = int(input())
    result = recursively_get_set(N)
    print(result)

