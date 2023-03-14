def row_check(board, row):
    return board[row] == 0

def col_check(board, col):
    pos = 1 << col
    for row in range(len(board)):
        if board[row] & pos:
            return False
    return True

def diagonal_check(board, row, col):
    left = right = 1 << col
    for i in range(len(board)):
        if row-i >= 0:
            if left < (1 << len(board)) and board[row-i] & left:
                return False
            if right > 0 and board[row-i] & right:
                return False
        if row+i < len(board):
            if left < (1 << len(board)) and board[row+i] & left:
                return False
            if right > 0 and board[row+i] & right:
                return False
        left <<= 1
        right >>= 1
    
    return True

def queen_valid(board, row, col):
    if row_check(board, row) and col_check(board, col) and diagonal_check(board, row, col):
        return True
    return False

def show_board(board, depth=0):
    format_str = '0' + str(len(board)) + 'b'
    for row in board:
        for i in range(depth):
            print("  ", end="")
        print(format(row, format_str))
    print()

def N_queens(n):
    board = [0] * n
    return count_queens_by_row(board)

def eight_queens():
    return N_queens(8)

def count_queens_by_row(board, row=0, depth=0):
    if row == len(board):
        show_board(board)
        return 1
    
    result = 0
    pos = 1
    for i in range(len(board)):
        if queen_valid(board, row, i):
            board[row] += pos
            result += count_queens_by_row(board, row+1, depth+1)
            board[row] -= pos
        pos <<= 1
    
    return result


if __name__ == '__main__':
    b = [0] * 8
    print(row_check(b, 0))
    print(col_check(b, 0))
    print(diagonal_check(b, 7, 7))
    show_board(b)

    b[0] = 1
    print(row_check(b, 0))
    print(col_check(b, 0))
    print(diagonal_check(b, 7, 7))
    show_board(b, 1)

    print(eight_queens())

    print(N_queens(5))