"""
https://www.acmicpc.net/problem/19591
"""

from collections import deque


def parse_text(T):
    result = deque()
    idx = 0
    initial_sign = 1
    if T[idx] == '-':
        initial_sign = -1
        idx += 1

    temp_num = 0
    while idx < len(T) and T[idx].isdigit():
        temp_num *= 10
        temp_num += int(T[idx])
        idx += 1
    result.append(temp_num * initial_sign)

    if idx < len(T):
        result.append(T[idx])
        idx += 1

        temp_num = 0
        while idx < len(T):
            if T[idx].isdigit():
                temp_num *= 10
                temp_num += int(T[idx])
            else:
                result.append(temp_num)
                temp_num = 0
                result.append(T[idx])
            idx += 1

        result.append(temp_num)

    return result


def calculate(a, b, c):
    if b == '+':
        return a+c
    elif b == '-':
        return a-c
    elif b == '*':
        return a*c
    elif b == '/':
        if a*c > 0:
            return a//c
        else:
            return a//c + 1


if __name__ == '__main__':
    # print(calculate(3, '/', 2))
    # print(3//2)
    #
    # print(calculate(-163, '/', 12))
    # print(-163//12)
    #
    # print(calculate(3, '/', -2))
    # print(3//-2)
    #
    # print(calculate(-30, '/', -12))
    # print(-30//-12)

    text = input()
    # print(text)
    l = parse_text(text)
    # print(l)

    while len(l) > 3:
        if l[1] in ('*', '/') and l[-2] in ('+', '-'):
            temp = calculate(l.popleft(), l.popleft(), l.popleft())
            l.appendleft(temp)

        elif l[1] in ('+', '-') and l[-2] in ('*', '/'):
            temp = [l.pop() for _ in range(3)]
            l.append(calculate(temp[2], temp[1], temp[0]))

        else:
            left = calculate(l[0], l[1], l[2])
            right = calculate(l[-3], l[-2], l[-1])
            if left > right:
                for _ in range(3):
                    l.popleft()
                l.appendleft(left)

            elif left < right:
                for _ in range(3):
                    l.pop()
                l.append(right)

            else:
                temp = calculate(l.popleft(), l.popleft(), l.popleft())
                l.appendleft(temp)

        # print(l)

    if len(l) == 3:
        print(calculate(l[0], l[1], l[2]))
    else:
        print(l[0])