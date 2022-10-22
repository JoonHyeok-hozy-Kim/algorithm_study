"""
https://www.acmicpc.net/problem/2866
"""

def same_string(B, str_len, c1, c2):
    for i in range(len(B) - str_len, len(B)):
        if B[i][c1] != B[i][c2]:
            return False
    return True


def top_to_bottom_sol(R, C, board):
    result = 0
    for j in range(R-1):
        diff_flag = True
        for a in range(C):
            for b in range(a+1, C):
                if same_string(board, R-1-j, a, b):
                    diff_flag = False
                    break
            if not diff_flag:
                break
        if diff_flag:
            result += 1
        else:
            break
    return result


def bottom_to_top_approach(R, C, board):
    max_level = 0
    for i in range(C):
        for j in range(i+1, C):
            level = 0
            while level < R:
                if board[R-1-level][i] == board[R-1-level][j]:
                    level += 1
                else:
                    max_level = max(max_level, level)
                    break
    return R - max_level - 1


if __name__ == '__main__':
    R, C = map(int, input().split())
    board = [input() for _ in range(R)]
    # print(board)

    # print(top_to_bottom_sol(R, C, board))
    print(bottom_to_top_approach(R, C, board))