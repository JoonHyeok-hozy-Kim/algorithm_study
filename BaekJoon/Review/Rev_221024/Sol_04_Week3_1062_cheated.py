""""
https://www.acmicpc.net/problem/1062
"""
from copy import deepcopy

DEFAULT = list('antatica')


def remove_repeat(L, exclude=None):
    buckets = {}
    if exclude is not None:
        for e in exclude:
            buckets[e] = -1
    for a in L:
        if a not in buckets:
            buckets[a] = 1
    if exclude is not None:
        for e in exclude:
            del buckets[e]
    return list(buckets.keys())


def recursive_solution(W, UA, target_cnt, al=[], i=0, result=0):
    if target_cnt == len(al):
        # print(al, get_possible_word_cnt(W, al))
        return max(result, get_possible_word_cnt(W, al))

    if i == len(UA):
        return result

    cal = deepcopy(al)
    cal.append(UA[i])

    temp = max(
        recursive_solution(W, UA, target_cnt, cal, i+1),
        recursive_solution(W, UA, target_cnt, al, i+1),
    )
    return max(temp, result)



def get_possible_word_cnt(W, al):
    result = 0
    for al_map_in_word in W:
        al_cnt = 0
        for a in al:
            if a in al_map_in_word:
                al_cnt += 1
        if al_cnt == len(W[al_map_in_word]):
            result += 1
    return result


if __name__ == '__main__':
    N, K = map(int, input().split())
    default = remove_repeat(DEFAULT)
    # print(default)

    word_map = {}
    alpha_map = {}

    for _ in range(N):
        w = input()
        w = w[4: len(w)-4]
        word_map[w] = {}
        for a in w:
            if a not in default:
                word_map[w][a] = 1
                if a not in alpha_map:
                    alpha_map[a] = {}
                alpha_map[a][w] = 1

    if K < len(default):
        print(0)

    else:
        used_alphabets = list(alpha_map.keys())
        # print(word_map)
        # print(alpha_map)
        # print(used_alphabets)
        # print(K-len(default))

        if len(used_alphabets) < K - len(default):
            print(N)

        else:
            print(recursive_solution(word_map, used_alphabets, K-len(default)))
