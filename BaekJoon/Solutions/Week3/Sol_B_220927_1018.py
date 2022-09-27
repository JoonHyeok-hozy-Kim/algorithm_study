"""
1018. 체스판 다시 칠하기
https://www.acmicpc.net/problem/1018
"""

BOARD_TYPE = ["WBWBWBWB", "BWBWBWBW"]

def paint_counter(board, x0, y0):
    cnt1 = 0
    cnt2 = 0
    for col in range(8):
        # print(BOARD_TYPE[col%2], BOARD_TYPE[(col+1)%2])
        for row in range(8):
            if board[y0+col][x0+row] != BOARD_TYPE[col%2][row]:
                cnt1 += 1
            if board[y0+col][x0+row] != BOARD_TYPE[(col+1)%2][row]:
                cnt2 += 1
    return min(cnt1, cnt2)

if __name__ == '__main__':
    M, N = map(int, input().split())
    board = []
    for _ in range(M):
        board.append(input())

    # print(board)
    result = None
    for i in range(M-7):
        for j in range(N-7):
            cnt = paint_counter(board, j, i)
            result = cnt if result is None else min(result, cnt)
    print(result)