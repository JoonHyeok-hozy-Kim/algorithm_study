"""
1285. 동전 뒤집기
https://www.acmicpc.net/problem/1285
"""
from copy import deepcopy

def show_coin_set(coin_set):
    N = len(coin_set)-1
    for i in range(N):
        print(bin(coin_set[i]).format())
    print(' [tail_cnt] : {}'.format(coin_set[-1]))


def count_tails(decimal):
    bin_num = bin(decimal)
    return bin_num.count('1')


def count_tails_coin_set(coin_set):
    N = len(coin_set)-1
    cnt = 0
    for i in range(N):
        cnt += count_tails(coin_set[i])
    return cnt


def _flip_row(decimal, N):
    result = ~decimal + (1<<(N))
    # print(bin(decimal), bin(result))
    return result


def flip_row(coin_set, row_idx):
    coin_set[row_idx] = _flip_row(coin_set[row_idx], len(coin_set)-1)
    coin_set[-1] = count_tails_coin_set(coin_set)
    return coin_set


def flip_col(coin_set, col_idx):
    N = len(coin_set)-1
    checker = pow(2, col_idx)
    for i in range(N):
        if coin_set[i] & checker:
            coin_set[i] -= checker
            coin_set[-1] -= 1
        else:
            coin_set[i] += checker
            coin_set[-1] += 1
    return coin_set


def inspect_row(coin_set):
    N = len(coin_set)-1
    for i in range(N):
        if count_tails(coin_set[i]) > N//2:
            yield i


def inspect_col(coin_set):
    N = len(coin_set)-1
    checker = 1
    for col_idx in range(N):
        cnt = 0
        for row_idx in range(N):
            if coin_set[row_idx] & checker:
                cnt += 1
        if cnt > N//2:
            yield col_idx
        checker *= 2


def recursive_operation(coin_set, depth=0):
    # show_coin_set(coin_set)
    min_tail = coin_set[-1]
    if depth == len(coin_set)-1:
        return min_tail

    # row_check = inspect_row(coin_set)
    for row in inspect_row(coin_set):
        c_coin_set = deepcopy(coin_set)
        c_coin_set = flip_row(c_coin_set, row)
        # print('-'*(depth+1), 'FLIP ROW', row)
        cand = recursive_operation(c_coin_set, depth+1)
        min_tail = min(min_tail, cand)

    for col in inspect_col(coin_set):
        c_coin_set = deepcopy(coin_set)
        c_coin_set = flip_col(c_coin_set, col)
        # print('-'*(depth+1), 'FLIP COL', col)
        cand = recursive_operation(c_coin_set, depth+1)
        min_tail = min(min_tail, cand)

    # print('-' * (depth + 1), 'min_tail :', min_tail)
    return min_tail



if __name__ == '__main__':
    N = int(input())
    coin_set = []
    tail_cnt = 0
    for _ in range(N):
        row = input()
        decimal_row = 0
        power = 1
        for c in row:
            if c == 'T':
                decimal_row += power
            power *= 2
        tail_cnt += count_tails(decimal_row)
        coin_set.append(decimal_row)
    coin_set.append(tail_cnt)

    result = recursive_operation(coin_set)
    print(result)


