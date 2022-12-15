"""
1946. 신입 사원
https://www.acmicpc.net/problem/1946
"""


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        score_board = [list(map(int, input().split())) for _ in range(N)]
        # print(score_board)
        score_board.sort()

        cnt = 1
        max_score_two = score_board[0][1]
        for i in range(N-1):
            if score_board[i+1][1] > max_score_two:
                continue
            else:
                cnt += 1
                max_score_two = score_board[i+1][1]

        print(cnt)