"""
https://www.acmicpc.net/problem/1018
"""
LINE_TYPE = [0b10101010, 0b1010101]


def line_check(ref_line, target_line):
    # print('{} vs {}'.format(bin(ref_line), bin(target_line)))
    diff_cnt = 0
    power = 1
    for i in range(8):
        ref = power & ref_line
        tgt = power & target_line
        if ref != tgt:
            diff_cnt += 1
        power *= 2

    return diff_cnt


if __name__ == '__main__':
    N, M = map(int, input().split())
    board = []

    # print(LINE_TYPE1[0], LINE_TYPE2[1])
    # print(line_check(LINE_TYPE[0], 0b01010101))
    # print(line_check(LINE_TYPE[0], 0b10101010))
    # print(line_check(LINE_TYPE[0], 0b10111010))

    for _ in range(N):
        line = input()
        temp, power = 0, 1
        for i in range(M):
            if line[M-1-i] == 'B':
                temp |= power
            power *= 2
        # print(bin(temp))
        board.append(temp)

    # print(board)
    result = None
    for i in range(N-7):
        p = 1
        for j in range(M-7):
            b1_diff = 0
            b2_diff = 0
            for row in range(8):
                target_line = board[row+i] // p
                # print(bin(target_line))
                if (result is None) or (result is not None and b1_diff < result):
                    b1_diff += line_check(LINE_TYPE[row%2], target_line)
                if (result is None) or (result is not None and b2_diff < result):
                    b2_diff += line_check(LINE_TYPE[(row+1)%2], target_line)

                if result is not None and b1_diff > result and b2_diff > result:
                    break
            temp = min(b1_diff, b2_diff)
            result = min(result, temp) if result is not None else temp
            p *= 2

    print(result)

