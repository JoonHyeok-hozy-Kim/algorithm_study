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


def recursively_operate_row(B, row, col=0, switch_cnt=0, check_above=True):
    if col == 10:
        if count_turned_on(B, row):
            return False, None, None
        if check_above and count_turned_on(B, row-1):
            return False, None, None
        return True, switch_cnt, B

    result = None
    NB = None
    CB = deepcopy(B)
    go_on1, cnt1, NB1 = recursively_operate_row(B, row, col+1, switch_cnt, check_above)
    if go_on1:
        result = cnt1
        NB = NB1

    click_switch(CB, row, col)
    go_on2, cnt2, NB2 = recursively_operate_row(CB, row, col+1, switch_cnt+1, check_above)

    if go_on2:
        if not(result is not None and result > cnt2):
            result = cnt2
            NB = NB2

    if result is not None:
        return True, result, NB
    else:
        return False, result, None


def first_two_rows_operation(B, cnt=0, switch_cnt=0):
    if cnt == 20:
        if count_turned_on(B, 0) > 0:
            return False, None, None
        return True, switch_cnt, B

    CB = deepcopy(B)
    result = None
    NB = None
    go_on1, cnt1, NB1 = first_two_rows_operation(B, cnt+1, switch_cnt)
    if go_on1:
        result = cnt1
        NB = NB1

    click_switch(CB, cnt//10, cnt%10)
    go_on2, cnt2, NB2 = first_two_rows_operation(CB, cnt+1, switch_cnt+1)
    if go_on2:
        if not(result is not None and result > cnt2):
            result = cnt2
            NB = NB2

    if result is not None:
        return True, result, NB
    else:
        return False, None, None



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
    board = [0] * 10
    show_board(board)

    for i in range(10):
        for j in range(10):
            click_switch(board, i, j)

    show_board(board)

