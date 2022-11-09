"""
https://www.acmicpc.net/problem/2630
"""


def validate_partition(S, x_start, y_start, length):
    first = S[y_start][x_start]
    for i in range(length):
        for j in range(length):
            if S[y_start+i][x_start+j] != first:
                return -1
    return first


def dnc_solution(S, x_start=None, y_start=None, length=None):
    if x_start is None:
        x_start = y_start = 0
        length = len(S)

    blue_cnt = white_cnt = 0

    temp = validate_partition(S, x_start, y_start, length)
    if temp == 0:
        white_cnt += 1
    elif temp == 1:
        blue_cnt += 1
    else:
        b1, w1 = dnc_solution(S, x_start, y_start, length//2)
        b2, w2 = dnc_solution(S, x_start+length//2, y_start, length//2)
        b3, w3 = dnc_solution(S, x_start, y_start+length//2, length//2)
        b4, w4 = dnc_solution(S, x_start+length//2, y_start+length//2, length//2)
        blue_cnt += (b1 + b2 + b3 + b4)
        white_cnt += (w1 + w2 + w3 + w4)

    return blue_cnt, white_cnt



if __name__ == '__main__':
    N = int(input())
    sheet = [list(map(int, input().split())) for _ in range(N)]
    # print(sheet)

    b, w = dnc_solution(sheet)
    print(w)
    print(b)