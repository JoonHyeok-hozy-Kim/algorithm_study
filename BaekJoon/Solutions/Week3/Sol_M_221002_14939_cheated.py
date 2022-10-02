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


def all_off_in_row(O, row):
    for i in range(10):
        if (row*10 + i) in O:
            return False
    return True


def turn_off_by_row(O, row):
    current_cnt = 0
    for i in range(10):
        if ((row-1)*10 + i) in O:
            current_cnt += 1
            turn_off(O, row*10 + i)
    return current_cnt


if __name__ == '__main__':
    on_map = {}
    cnt = 0
    for i in range(10):
        row = input()
        for bulb in row:
            if bulb == 'O':
                on_map[cnt] = 1
            cnt += 1

    switch_cnt = None
    for i in range(1<<10):
        c_on_map = deepcopy(on_map)
        temp_cnt = 0
        for j in range(10):
            if i & (1<<j):
                temp_cnt += 1
                turn_off(c_on_map, j)

        # display_bulbs(c_on_map)

        for k in range(9):
            if switch_cnt is not None and temp_cnt >= switch_cnt:
                break
            temp_cnt += turn_off_by_row(c_on_map, k+1)
            # display_bulbs(c_on_map)

        if all_off_in_row(c_on_map, 9):
            switch_cnt = min(switch_cnt, temp_cnt) if switch_cnt is not None else temp_cnt

    print(switch_cnt) if switch_cnt is not None else print(-1)


