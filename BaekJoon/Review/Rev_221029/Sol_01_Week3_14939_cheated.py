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


def recursively_operate_row(B, switch_cnt, prev_min=None, row=1):
    if row == 10:
        if count_turned_on(B) == 0:
            return True, switch_cnt
        return False, None

    # CB = deepcopy(B)

    for j in range(10):
        if B[row-1] & (1 << (9-j)):
            click_switch(B, row, j)
            switch_cnt += 1

    if prev_min is not None and switch_cnt > prev_min:
        return False, None

    go_on, total_cnt = recursively_operate_row(B, switch_cnt, prev_min, row+1)
    if go_on:
        # print('Row : {}'.format(row))
        # show_board(CB)
        return True, total_cnt
    return False, None


def first_rows_operation(B, cnt=0, switch_cnt=0):
    if cnt == 10:
        # show_board(B)
        return [[B, switch_cnt]]

    result_list = []
    CB = deepcopy(B)
    result_list.extend(first_rows_operation(B, cnt+1, switch_cnt))

    click_switch(CB, 0, cnt)
    result_list.extend(first_rows_operation(CB, cnt+1, switch_cnt+1))

    return result_list



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

    F = first_rows_operation(board)

    result = None
    for l in F:
        # show_board(B)
        go_on, cnt = recursively_operate_row(l[0], l[1], result)
        if go_on:
            result = min(result, cnt) if result is not None else cnt

    if result is not None:
        print(result)
    else:
        print(-1)


"""
#O########
#O########
#O########
#O########
#O########
#O########
#O########
#O########
#O########
#O########

##########
##########
##########
####OO####
###O##O###
####OO####
##########
##########
##########
##########

OO########
O#########
##########
##########
##########
##########
##########
##########
##########
##########

OO########
O#########
##########
##########
##########
##########
##########
##########
#########O
########OO
"""