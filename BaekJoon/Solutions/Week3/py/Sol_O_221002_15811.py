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
        n1 = P[CM[W[0][-1-j]]]
        n2 = P[CM[W[1][-1-j]]]
        n3 = P[CM[W[2][-1-j]]]
        if (n1+n2+add_up)%10 != n3:
            return False
        add_up = (n1+n2)//10

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

    for w in words:
        for c in w:
            char_map[c] = None

    cnt = 0
    for c in char_map:
        char_map[c] = cnt
        cnt += 1

    result = try_with_permutations(words, char_map)
    print(result)

