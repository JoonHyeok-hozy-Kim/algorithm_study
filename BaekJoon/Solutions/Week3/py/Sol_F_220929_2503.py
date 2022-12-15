"""
2503. 숫자야구
https://www.acmicpc.net/problem/2503
"""
from copy import deepcopy


def recursive_set_builder(num_set, rep, cnt=0):
    if rep == cnt:
        return num_set

    new_num_set = []
    while len(num_set) > 0:
        e = num_set.pop()
        for i in range(1, 10):
            if i not in e:
                ec = deepcopy(e)
                ec.append(i)
                new_num_set.append(ec)

    return recursive_set_builder(new_num_set, rep, cnt+1)


def play_game(num_set, call, S, B):
    filtered = []
    while len(num_set) > 0:
        e = num_set.pop()
        s_idxes = []
        b_cnt = 0

        for i in range(3):
            if call[i] == e[i]:
                s_idxes.append(i)

        if len(s_idxes) == S:
            for i in range(3):
                if i not in s_idxes and call[i] in e:
                    b_cnt += 1
            if b_cnt == B:
                filtered.append(e)

    return filtered




if __name__ == '__main__':
    N = int(input())
    num_set = [[]]
    num_set = recursive_set_builder(num_set, 3)

    for game in range(N):
        call, S, B = map(int, input().split())
        call_list = []
        call_list.append(call//100)
        call %= 100
        call_list.append(call//10)
        call_list.append(call%10)
        num_set = play_game(num_set, call_list, S, B)
        # print(str(call), S, B, num_set)

    # print(num_set)
    print(len(num_set))
