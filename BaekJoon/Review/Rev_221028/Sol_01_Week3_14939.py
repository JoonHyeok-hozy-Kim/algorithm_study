"""
https://www.acmicpc.net/problem/14939
"""

from copy import deepcopy


def show_board(B):
    for i in range(10):
        power = 1<<9
        for j in range(10):
            if B[i] & power:
                print('O', end="")
            else:
                print('#', end="")
            power //= 2
        print()
    print()


def turn_on_off(B, i, j):
    if B[i] & (1 << 9-j):
        B[i] -= (1 << 9-j)
    else:
        B[i] += (1 << 9-j)


def click_switch(B, i, j):
    turn_on_off(B, i, j)
    if i > 0:
        turn_on_off(B, i-1, j)
    if i < 9:
        turn_on_off(B, i+1, j)
    if j > 0:
        turn_on_off(B, i, j-1)
    if j < 9:
        turn_on_off(B, i, j+1)


def count_turned_on(B, row=None):
    cnt = 0
    for i in range(10):
        if row is not None and i != row:
            continue
        for j in range(10):
            if B[i] & (1<<j):
                cnt += 1
    return cnt


def operate_row(B, row):
    None


if __name__ == '__main__':
    board = []
    for i in range(10):
        line = input()
        num_line = 0
        for j in range(10):
            if line[9-j] == 'O':
                num_line += 1 << j
        board.append(num_line)

    # print(board)
    # show_board(board)

    # Starting from row zero



    # Starting from row one

