"""
https://www.acmicpc.net/problem/4658
"""


def play(T):
    length_map = {}
    triangle_usage_map = {0: True}
    min_sum_inners = None

    for i in range(1, 6):
        for l in T[i]:
            if l not in length_map:
                length_map[l] = []
            length_map[l].append(i)

        triangle_usage_map[i] = False

    # print('length_map : {}'.format(length_map))
    # print('triangle_usage_map : {}'.format(triangle_usage_map), end="\n")

    for j in range(3):
        # print('GAME {}. [{}, {}]'.format(j+1, T[0][j], T[0][(j+1)%3]))
        go_on, temp_sum_inner = recursive_play(T, length_map, triangle_usage_map, [T[0][j], T[0][(j+1)%3]])
        if go_on:
            min_sum_inners = min(min_sum_inners, temp_sum_inner) if min_sum_inners is not None else temp_sum_inner

    # print('RESULT : {}'.format(min_sum_inners))
    return min_sum_inners


def recursive_play(T, L, t, inner=[]):
    if len(inner) == 7:
        if inner[0] == inner[-1]:
            # print('CANDIDATE : {}'.format(inner))
            return True, sum(inner) - inner[0]
        else:
            return False, None


    if inner[-1] not in L:
        return False, None

    temp_min_sum_inners = None
    for i in L[inner[-1]]:
        if not t[i]:
            inner.append(T[i][(T[i].index(inner[-1])+1)%3])
            t[i] = True
            go_on, temp_sum = recursive_play(T, L, t, inner)
            if go_on:
                temp_min_sum_inners = min(temp_min_sum_inners, temp_sum) if temp_min_sum_inners is not None else temp_sum
            t[i] = False
            inner.pop()

    if temp_min_sum_inners is not None:
        return True, temp_min_sum_inners

    else:
        return False, None


if __name__ == '__main__':
    sign = None
    answer_list = []
    while sign != '$':
        triangle_set = [list(map(int, input().split())) for _ in range(6)]
        # print(triangle_set)

        inner_sum = play(triangle_set)

        if inner_sum is None:
            answer_list.append('none')

        else:
            result = 0
            for t in triangle_set:
                result += sum(t)
            result -= inner_sum * 2
            answer_list.append(result)

        sign = input()

    for i in answer_list:
        print(i)