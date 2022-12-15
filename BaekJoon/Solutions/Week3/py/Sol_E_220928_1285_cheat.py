"""
1285. 동전 뒤집기
https://www.acmicpc.net/problem/1285
"""


if __name__ == '__main__':
    N = int(input())
    result = None
    original_board = [input() for _ in range(N)]
    reversed_board = []
    for row in original_board:
        rev_row = []
        for c in row:
            rev_row.append('F') if c == 'T' else rev_row.append('T')
        reversed_board.append(''.join(rev_row))

    # print('ORG : {}'.format(original_board))
    # print('REV : {}'.format(reversed_board))

    for b in range(1<<N):
        temp_board = []
        for i in range(N):
            if b & (1<<i):
                temp_board.append(reversed_board[i])
            else:
                temp_board.append(original_board[i])

        # print('TEM : {}'.format(temp_board))

        cnt = 0
        for col in range(N):
            col_cnt = 0
            for row in range(N):
                if temp_board[row][col] == 'T':
                    col_cnt += 1
            cnt += min(col_cnt, N-col_cnt)

        result = cnt if result is None else min(result, cnt)

    print(result)