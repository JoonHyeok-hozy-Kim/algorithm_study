"""
14939. 불 끄기
https://www.acmicpc.net/problem/14939
"""
from collections import deque
from copy import deepcopy


def display_bulbs(O, indent=0):
    print()
    for j in range(indent*2): print(' ', end="")
    for i in range(10):
        print('-', end="")
    for i in range(100):
        if i%10 == 0:
            print()
            for j in range(indent*2): print(' ', end="")
        if i in O:
            print('O', end="")
        else:
            print('#', end="")
    print()
    for j in range(indent*2): print(' ', end="")
    for i in range(10):
        print('-', end="")
    print()


def switch(O, i):
    if i in O:
        del O[i]
    else:
        O[i] = 1


def adjacent_to(i):
    yield i
    if i//10 > 0:
        yield i-10
    if i%10 > 0:
        yield i-1
    if i%10 < 9:
        yield i+1
    if i//10 < 9:
        yield i+10


def turn_off(O, i):
    # print('In turn_off, i : {}'.format(i))
    for j in adjacent_to(i):
        switch(O, j)


def on_count_by_row(O, row):
    # print('In on_count_by_row, row : {}'.format(row))
    result = 0
    for i in range(10):
        if (row*10 + i) in O:
            result += 1
    return result


def recursive_turn_off_by_row(O, row, depth=0, switch_cnt=0):
    # print('In recursive_turn_off_by_row, row : {}, depth : {}, switch_cnt : {}'.format(row, depth, switch_cnt))
    # display_bulbs(O, depth)
    depth_limit = 20 if row == 1 else 10
    # if row == 8:
    #     on_count = on_count_by_row(O, row-1) + on_count_by_row(O, row) + on_count_by_row(O, row+1)

    if row == 9:
        on_count = on_count_by_row(O, row-1) + on_count_by_row(O, row)
    else:
        on_count = on_count_by_row(O, row-1)

    if on_count == 0:
        return True, switch_cnt, O
    elif depth == depth_limit:
        return False, None, None

    temp_switch_cnt, temp_O = None, None

    # Case 1. Skip
    O_copy = deepcopy(O)
    go_on_one, switch_cnt_one, O_one = recursive_turn_off_by_row(O_copy, row, depth+1, switch_cnt)
    if go_on_one:
        temp_switch_cnt, temp_O = switch_cnt_one, O_one

    # Case 2. Switch
    if row == 1:
        target = (row-1)*10 + depth
    else:
        target = row*10 + depth

    turn_off(O, target)

    # if row == 8:
    #     temp_on_count = on_count_by_row(O, row-1) + on_count_by_row(O, row) + on_count_by_row(O, row+1)

    if row == 9:
        temp_on_count = on_count_by_row(O, row-1) + on_count_by_row(O, row)
    else:
        temp_on_count = on_count_by_row(O, row-1)

    if temp_on_count < on_count:
        # print('SWITCH : {}'.format(depth))
        O_copy = deepcopy(O)
        go_on_two, switch_cnt_two, O_two = recursive_turn_off_by_row(O_copy, row, depth+1, switch_cnt+1)
        if go_on_two:
            if temp_switch_cnt is None or temp_switch_cnt > switch_cnt_two:
                temp_switch_cnt, temp_O = switch_cnt_two, O_two
            elif temp_switch_cnt == switch_cnt_two:
                on_count1 = on_count_by_row(O_one, row)
                on_count2 = on_count_by_row(O_two, row)
                if on_count1 > on_count2:
                    temp_switch_cnt, temp_O = switch_cnt_two, O_two
    # turn_off(O, target)

    if temp_switch_cnt is not None:
        return True, temp_switch_cnt, temp_O
    else:
        return False, None, None


def call_by_rows(O):
    total_cnt = 0
    for r in range(1, 10):
        go_on, temp_cnt, new_O = recursive_turn_off_by_row(O, r)
        if go_on:
            total_cnt += temp_cnt
            O = new_O
            # display_bulbs(O, r)
        else:
            return -1

    if go_on:
        # display_bulbs(new_O)
        return total_cnt + temp_cnt
    else:
        return -1




if __name__ == '__main__':
    on_map = {}
    cnt = 0
    for i in range(10):
        row = input()
        for bulb in row:
            if bulb == 'O':
                on_map[cnt] = 1
            cnt += 1

    # display_bulbs(on_map)
    # turn_off(on_map, 11)
    # display_bulbs(on_map)


    result = call_by_rows(on_map)
    print(result)

    # a, b, c = recursive_turn_off_by_row(on_map, 1)
    # if a:
    #     print(b)
    #     display_bulbs(c)