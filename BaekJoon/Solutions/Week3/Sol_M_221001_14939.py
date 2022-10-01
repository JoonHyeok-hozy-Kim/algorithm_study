"""
14939. 불 끄기
https://www.acmicpc.net/problem/14939
"""


def display_bulbs(O, indent=0):
    print()
    for j in range(indent): print(' ', end="")
    for i in range(10):
        print('-', end="")
    for i in range(100):
        if i%10 == 0:
            print()
            for j in range(indent): print(' ', end="")
        if i in O:
            print('O', end="")
        else:
            print('#', end="")
    print()
    for j in range(indent): print(' ', end="")
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
    for bulb in adjacent_to(i):
        switch(O, bulb)


def recursive_turn_off(O, depth=0, min_switch_count=None):
    # print('min_switch_count : {}'.format(min_switch_count))
    # display_bulbs(O, depth)
    if min_switch_count is not None and depth >= min_switch_count:
        return False, None

    on_count = len(O)
    if on_count == 0:
        return True, depth

    try_count = 0

    for i in range(100):
        turn_off(O, i)
        new_count = len(O)
        if new_count < on_count:
            try_count += 1
            # print('-> Turn off ({},{})'.format(i//10, i%10))
            go_on, temp_switch_count = recursive_turn_off(O, depth+1, min_switch_count)
            if go_on:
                min_switch_count = min(min_switch_count, temp_switch_count) if min_switch_count is not None else temp_switch_count
        turn_off(O, i)

    if try_count == 0:
        return False, None

    return True, min_switch_count


def recursive_turn_off_filtered(O, depth=0, min_switch_count=None):
    # print('min_switch_count : {}'.format(min_switch_count))
    # display_bulbs(O, depth)
    if min_switch_count is not None and depth >= min_switch_count:
        return False, None

    on_count = len(O)
    if on_count == 0:
        return True, depth

    try_count = 0

    for key in O.keys():
        for i in adjacent_to(key):
            turn_off(O, i)
            new_count = len(O)
            if new_count < on_count:
                try_count += 1
                # print('-> Turn off ({},{})'.format(i//10, i%10))
                go_on, temp_switch_count = recursive_turn_off_filtered(O, depth+1, min_switch_count)
                if go_on:
                    min_switch_count = min(min_switch_count, temp_switch_count) if min_switch_count is not None else temp_switch_count
            turn_off(O, i)

    if try_count == 0:
        return False, None

    return True, min_switch_count




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

    finale, switch_cnt = recursive_turn_off(on_map)
    # finale, switch_cnt = recursive_turn_off_filtered(on_map)
    if finale:
        print(switch_cnt)
    else:
        print(-1)