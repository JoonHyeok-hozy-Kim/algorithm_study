"""
https://www.acmicpc.net/problem/15811
"""
from random import randint


def temp_validation(S, M):
    for s in S:
        if s[0] is not None and s[1] is not None and s[2] is not None:
            if M[s[0]] is not None and M[s[1]] is not None and M[s[2]] is not None:
                if (M[s[0]] + M[s[1]])%10 not in (M[s[2]], (M[s[2]]+9)%10):
                    # print('TEMP VALIDATED, M : {}'.format(M))
                    # print('{} + {} , {}'.format(M[s[0]], M[s[1]], M[s[2]]), end="\n\n")
                    return False
    return True


def generate_num(w, M):
    result = 0
    for c in w:
        result *= 10
        result += M[c]
    return result


def validate(W, M):
    return generate_num(W[0], M) + generate_num(W[1], M) == generate_num(W[2], M)


def recursive_solution(W, M, L, S, cnt=0, used=[]):
    # print('M : {}'.format(M))
    if not temp_validation(S, M):
        return False

    if cnt == len(M):
        # print('M : {}'.format(M))
        return validate(W, M)

    for i in range(10):
        if i not in used:
            M[L[cnt]] = i
            used.append(i)
            # print(used)

            if recursive_solution(W, M, L, S, cnt+1, used):
                return True

            M[L[cnt]] = None
            used.pop()

    return False



if __name__ == '__main__':
    words = input().split()
    max_len = 0

    # words = []
    # for i in range(3):
    #     w_list = []
    #     for j in range(18):
    #         w_list.append(chr(randint(65, 74)))
    #     words.append(''.join(w_list))
    # print(words)

    alpha_map = {}
    # print(words)

    for w in words:
        max_len = max(max_len, len(w))
        for c in w:
            alpha_map[c] = None

    set_by_digit = [[None] * 3 for _ in range(max_len)]
    for i in range(len(words)):
        for j in range(len(words[i])):
            set_by_digit[max_len - 1 - j][i] = words[i][len(words[i]) - 1 - j]

    # print(set_by_digit)


    if len(alpha_map) > 10:
        print('NO')

    else:
        nums = [i for i in range(10)]
        alpha_list = list(alpha_map.keys())

        if recursive_solution(words, alpha_map, alpha_list, set_by_digit):
            print('YES')
        else:
            print('NO')
