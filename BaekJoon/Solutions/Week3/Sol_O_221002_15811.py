"""
15811. 복면산?!
https://www.acmicpc.net/problem/15811
"""
from itertools import permutations

def equation_validation(W, CM, P):
    min_len = min([len(W[i]) for i in range(3)])
    # print(min_len)
    add_up = 0

    for j in range(min_len):
        a = P[CM[W[0][-1-j]]]
        b = P[CM[W[1][-1-j]]]
        c = P[CM[W[2][-1-j]]]
        if (a+b+add_up)%10 != c:
            return False
        add_up = (a+b)//10

    last_nums = [0] * 3
    for k in range(3):
        if len(W[k]) > min_len:
            L = len(W[k])-min_len
            power = 1
            for m in range(L):
                last_nums[k] += P[CM[W[k][L-1-m]]] * power
                power *= 10

    if last_nums[0] + last_nums[1] + add_up != last_nums[2]:
        return False

    return True


def try_with_permutations(W, CM):
    perms = permutations([i for i in range(10)], len(char_map))
    for p in perms:
        if equation_validation(words, char_map, p):
            return 'YES'
    return 'NO'


if __name__ == '__main__':
    char_map = {}
    words = list(input().split())
    conditions = []
    # print(words)

    for w in words:
        for c in w:
            char_map[c] = None

    # print(char_map)
    cnt = 0
    for c in char_map:
        char_map[c] = cnt
        cnt += 1
    # print(char_map)


    # equation_validation(words, char_map)

    print(try_with_permutations(words, char_map))

