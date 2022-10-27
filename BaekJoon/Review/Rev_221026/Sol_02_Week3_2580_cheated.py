"""
https://www.acmicpc.net/problem/2580
"""


def check_row(B, i, k):
    for j in range(9):
        if B[i][j] == k:
            return False
    return True


def check_col(B, j, k):
    for i in range(9):
        if B[i][j] == k:
            return False
    return True


def check_partition(B, i, j, k):
    row_start = (i//3) * 3
    col_start = (j//3) * 3
    for m in range(3):
        for n in range(3):
            if B[row_start+m][col_start+n] == k:
                return False
    return True


def dfs(B, b, idx=0):
    # show_board(B)
    if idx == len(b):
        return True, B

    for k in range(1, 10):
        x, y = b[idx][0], b[idx][1]

        if check_row(B, x, k) and check_col(B, y, k) and check_partition(B, x, y, k):
            B[x][y] = k
            go_on, result = dfs(B, b, idx+1)
            if go_on:
                return True, result

            B[x][y] = 0

    return False, None



def show_board(B):
    if B is None:
        return
    for i in range(len(B)):
        # print(*B[i], sep=" ")
        print(' '.join(B[i]))


if __name__ == '__main__':
    board = [list(map(int, input().split())) for _ in range(9)]
    # show_board(board)

    blanks = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                blanks.append([i, j])
    # print(blanks)

    finale, filled = dfs(board, blanks)

    if finale:
        for i in board:
            print(*i, sep=" ")

"""
0 0 5 3 0 0 0 0 0
8 0 0 0 0 0 0 2 0
0 7 0 0 1 0 5 0 0
4 0 0 0 0 5 3 0 0
0 1 0 0 7 0 0 0 6
0 0 3 2 0 0 0 8 0
0 6 0 5 0 0 0 0 9
0 0 4 0 0 0 0 3 0
0 0 0 0 0 9 7 0 0
"""