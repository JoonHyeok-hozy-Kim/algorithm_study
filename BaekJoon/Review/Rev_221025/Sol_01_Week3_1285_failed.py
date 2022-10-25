"""
https://www.acmicpc.net/problem/1285
"""

from copy import deepcopy


def translate_into_binary(line):
    result = 0
    for c in line:
        if c == 'H':
            result += 1
        result *= 2
    return result // 2


def flip_row(C, r_idx):
    original = C[r_idx]
    start_with_tail = False
    if original < 2 << len(C):
        original += 2 << len(C)
        start_with_tail = True
    flipped = ~ original
    if start_with_tail:
        flipped += 2 << len(C)
    C[r_idx] = flipped


def flip_col(C, c_idx):
    for i in range(len(C)):
        original = C[i]
        temp = original >> (len(C) - c_idx - 1)
        if temp % 2 == 1:
            C[i] -= 1 << (len(C) - c_idx - 1)
        else:
            C[i] += 1 << (len(C) - c_idx - 1)


def display(C):
    for i in range(len(C)):
        target = C[i]
        line_text = []
        for j in range(len(C)):
            line_text.append('H') if target % 2 == 1 else line_text.append('T')
            target //= 2
        print(''.join(reversed(line_text)))
    print()


def tail_cnt(C):
    result = 0
    for i in range(len(C)):
        line = C[i]
        for j in range(len(C)):
            if line % 2 == 0:
                result += 1
            line //= 2
    return result


def recursive_solution(C, curr_num_tail=None):
    # display(C)
    if curr_num_tail is None:
        curr_num_tail = tail_cnt(C)

    min_num_tail = curr_num_tail
    for i in range(len(C)):
        flip_row(C, i)
        new_num_tail = tail_cnt(C)
        if new_num_tail < curr_num_tail:
            # print('flip_row {}'.format(i))
            CC = deepcopy(C)
            min_num_tail = min(min_num_tail, recursive_solution(CC, new_num_tail))
        flip_row(C, i)

    for j in range(len(C)):
        CC = deepcopy(C)
        flip_col(CC, j)
        new_num_tail = tail_cnt(CC)
        if new_num_tail < curr_num_tail:
            # print('flip_col {}'.format(j))
            min_num_tail = min(min_num_tail, recursive_solution(CC, new_num_tail))

    return min_num_tail


def one_loop_solution(C):
    original_tail_num = tail_cnt(C)
    for i in range(len(C)):
        flip_row(C, i)
        new_tail_num = tail_cnt(C)
        if original_tail_num < new_tail_num:
            flip_row(C, i)
        else:
            original_tail_num = new_tail_num

    for j in range(len(C)):
        flip_col(C, j)
        new_tail_num = tail_cnt(C)
        if original_tail_num < new_tail_num:
            flip_col(C, j)
        else:
            original_tail_num = new_tail_num

    return original_tail_num


if __name__ == '__main__':
    N = int(input())
    coins = [translate_into_binary(input()) for _ in range(N)]
    # print(coins)
    # display(coins)

    print(recursive_solution(coins))
    print(one_loop_solution(coins))