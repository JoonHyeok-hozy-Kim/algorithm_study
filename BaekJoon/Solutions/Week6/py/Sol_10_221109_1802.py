"""
https://www.acmicpc.net/problem/1802
"""


def type_one_folding(prev):
    result = []
    cnt = 0
    for i in range(len(prev)):
        if cnt % 2 == 0:
            result.append('1')
        else:
            result.append('0')

        result.append(prev[i])
        cnt += 1

    if cnt % 2 == 0:
        result.append('1')
    else:
        result.append('0')

    return ''.join(result)


def type_two_folding(prev):
    result = []
    cnt = 0
    for i in range(len(prev)):
        if cnt % 2 == 0:
            result.append('0')
        else:
            result.append('1')

        result.append(prev[i])
        cnt += 1

    if cnt % 2 == 0:
        result.append('0')
    else:
        result.append('1')

    return ''.join(result)


def reset_type_one(curr):
    idx = 0
    result = []
    cnt = 0
    while idx < len(curr):
        if (cnt % 2 == 0 and curr[idx] == '1') or (cnt % 2 == 1 and curr[idx] == '0'):
            if idx == len(curr) -1:
                break
            else:
                idx += 1
                cnt += 1
        else:
            return False, None

        if idx == len(curr):
            return False, None
        else:
            result.append(curr[idx])
            idx += 1

    return True, ''.join(result)


def reset_type_two(curr):
    idx = 0
    result = []
    cnt = 0
    while idx < len(curr):
        if (cnt % 2 == 0 and curr[idx] == '0') or (cnt % 2 == 1 and curr[idx] == '1'):
            if idx == len(curr) -1:
                break
            else:
                idx += 1
                cnt += 1
        else:
            return False, None

        if idx == len(curr):
            return False, None
        else:
            result.append(curr[idx])
            idx += 1

    return True, ''.join(result)


def figure_out(T):
    while len(T) > 0:
        # print(T)
        if T[0] == '1':
            # print('type1')
            go_on, T = reset_type_one(T)

        else:
            # print('type2')
            go_on, T = reset_type_two(T)

        if not go_on:
            return 'NO'

    return 'YES'


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print(figure_out(input()))

    # temp1 = ''
    # for i in range(5):
    #     temp1 = type_one_folding(temp1)
    #     print(temp1)
    #
    # for i in range(5):
    #     go_on, temp1 = reset_type_one(temp1)
    #     print(temp1)
    #
    # temp2 = ''
    # for i in range(6):
    #     temp2 = type_two_folding(temp2)
    #     print(temp2)
    #
    # for i in range(6):
    #     go_on, temp2 = reset_type_two(temp2)
    #     print(temp2)