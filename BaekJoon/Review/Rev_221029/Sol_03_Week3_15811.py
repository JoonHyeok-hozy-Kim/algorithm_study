"""
https://www.acmicpc.net/problem/15811
"""

from copy import deepcopy
from itertools import permutations


def generate_number(AM, w, length=None):
    if length is None:
        length= len(w)
    power = 1
    result = 0
    # print('In generate_number, w : {}, length : {}'.format(w, length))
    # print('AM : {}'.format(AM))
    for i in range(length):
        result += AM[w[len(w) - 1 - i]] * power
        power *= 10
    return result


def validate(AM, W, length=None):
    # print('In validate, W : {}'.format(W))
    num1 = generate_number(AM, W[0], length)
    num2 = generate_number(AM, W[1], length)
    num3 = generate_number(AM, W[2], length)
    if length is not None:
        power = pow(10, length)
        return (num1 + num2) % power == num3 % power

    return num1 + num2 == num3


def no_none_in_map(AM):
    for k in AM:
        if AM[k] is None:
            return False
    return True


def recursive_solution(AM, AO, W, NUMS, cnt=0):
    # for i in range(cnt):
    #     print('  ', end="")
    # print('In recursive_solution, cnt : {}, AM : {}'.format(cnt, AM))

    if cnt == len(AO) or no_none_in_map(AM):
        if validate(AM, W):
            return True
        return False

    for i in range(len(NUMS)):
        # print('AO[cnt] : {}, value : {}'.format(AO[cnt], AM[AO[cnt]]))
        if AM[AO[cnt]] is None:
            CAM = deepcopy(AM)
            CN = deepcopy(NUMS)
            CAM[AO[cnt]] = CN.pop(i)

            if cnt % 3 == 2:
                if not validate(CAM, W, cnt//3 + 1):
                    continue

            if recursive_solution(CAM, AO, W, CN, cnt+1):
                return True

        else:
            if recursive_solution(AM, AO, W, NUMS, cnt+1):
                return True

    return False




if __name__ == '__main__':
    words = input().split()
    # print(words)

    alpha_map = {}
    WL = 0
    for w in words:
        WL = max(WL, len(w))
        for c in w:
            alpha_map[c] = None
    alpha_list = list(alpha_map.keys())
    # print(alpha_map)
    # print(alpha_list)

    alpha_in_order = []
    for digit in range(WL):
        for w in words:
            if len(w) > digit:
                alpha_in_order.append(w[len(w)-1-digit])
                # print(alpha_in_order)

    nums = [i for i in range(10)]

    result = recursive_solution(alpha_map, alpha_in_order, words, nums)

    if result:
        print('YES')
    else:
        print('NO')