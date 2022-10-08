"""
11660. 구간 합 구하기 5
https://www.acmicpc.net/problem/11660
"""

def get_summed_board(B, N):
    result_board = [[None] * N for _ in range(N)]
    temp_sum = 0
    for i in range(N):
        temp_sum += B[0][i]
        result_board[0][i] = temp_sum
    temp_sum = 0
    for j in range(N):
        temp_sum += B[j][0]
        result_board[j][0] = temp_sum
    for i in range(1, N):
        for j in range(1, N):
            result_board[i][j] = B[i][j] + result_board[i-1][j] + result_board[i][j-1] - result_board[i-1][j-1]
    return result_board


def get_partial_sum(SB, xy_list):
    result = SB[xy_list[2]-1][xy_list[3]-1]
    if xy_list[0] > 1:
        result -= SB[xy_list[0]-2][xy_list[3]-1]
    if xy_list[1] > 1:
        result -= SB[xy_list[2]-1][xy_list[1]-2]
    if xy_list[0] > 1 and xy_list[1] > 1:
        result += SB[xy_list[0]-2][xy_list[1]-2]
    return result


if __name__ == '__main__':
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    cases = [list(map(int, input().split())) for _ in range(M)]
    # print(board, cases)

    sum_board = get_summed_board(board, N)
    # print(sum_board)

    for xy in cases:
        print(get_partial_sum(sum_board, xy))