"""
10164. 격자상의 경로
https://www.acmicpc.net/problem/10164
"""

def get_board(heigth, width):
    B = [[1] * width for _ in range(heigth)]
    for i in range(heigth):
        for j in range(width):
            if i > 0 and j > 0:
                B[i][j] = B[i-1][j] + B[i][j-1]
    return B


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    # print(N, M, K)

    if K == 0:
        board = get_board(N, M)
        print(board[N-1][M-1])

    else:
        h1 = (K-1)//M + 1
        w1 = K % M if K % M > 0 else M
        h2, w2 = N - h1 + 1, M - w1 + 1

        mh, mw = max(h1, h2), max(w1, w2)
        board = get_board(mh, mw)
        print(board[h1-1][w1-1] * board[h2-1][w2-1])
