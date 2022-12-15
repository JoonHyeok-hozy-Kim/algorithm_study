"""
2580. 스도쿠
https://www.acmicpc.net/problem/2580
"""


def check_row(B, x, a):
    for k in range(9):
        if a == B[x][k]:
            return False
    return True


def check_col(B, y, a):
    for k in range(9):
        if a == B[k][y]:
            return False
    return True


def check_partition(B, x, y, a):
    x_start = x // 3 * 3
    y_start = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == B[x_start+i][y_start+j]:
                return False
    return True


def dfs(B, b, idx):
    if idx == len(b):
        # for i in range(9):
        #     print(*B[i])
        return True, B

    for k in range(1, 10):
        x = b[idx][0]
        y = b[idx][1]

        if check_row(B, x, k) and check_col(B, y, k) and check_partition(B, x, y, k):
            B[x][y] = k
            go_on, B = dfs(B, b, idx+1)
            if go_on:
                return True, B
            else:
                B[x][y] = 0

    return False, B


if __name__ == '__main__':
    board = [list(map(int, input().split())) for _ in range(9)]
    blanks = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                blanks.append((i, j))

    finale, board = dfs(board, blanks, 0)
    if finale:
        for _ in range(9):
            print(*board[_])

