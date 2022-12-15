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

        score_board = sorted(score_board)
        # print(score_board)

        candidates = []
        candidates.append(score_board.pop(0))
        score_two_max = candidates[0][1]
        cnt = 1
        while len(score_board) > 0:
            target = score_board.pop(0)
            # print(target, candidates, score_one_bound, score_two_bound)
            if target[1] > score_two_max:
                continue
            else:
                score_two_max = target[1]
                cnt += 1

        print(cnt)
