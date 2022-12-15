"""
1541. 잃어버린 괄호
https://www.acmicpc.net/problem/1541
"""


def parse_equation(E):
    temp = 0
    result_list = []
    for i in range(len(E)):
        if E[i] in ('+', '-'):
            result_list.append(temp)
            temp = 0
            result_list.append(E[i])
        else:
            temp *= 10
            temp += int(E[i])
    result_list.append(temp)
    return result_list


if __name__ == '__main__':
    eq = input()
    eql = parse_equation(eq)
    # print(eql)
    S = []
    S.append(eql.pop(0))

    while len(eql) > 0:
        curr = eql.pop(0)
        if curr == '-':
            S.append(eql.pop(0))
        elif curr == '+':
            temp = S.pop()
            temp += eql.pop(0)
            S.append(temp)

    result = S.pop(0)
    while len(S) > 0:
        result -= S.pop(0)
    print(result)