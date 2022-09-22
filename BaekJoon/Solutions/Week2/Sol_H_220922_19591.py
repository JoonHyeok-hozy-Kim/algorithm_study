"""
19591. 독특한 계산기
https://www.acmicpc.net/problem/19591
"""
from collections import deque
import sys
sys.setrecursionlimit(10**6)

MUL_DIV = ['*', '/']

def text_parser(text):
    if len(text) == 0:
        return ''
    if text[0] == '-':
        idx = 1
        first_sign = -1
    else:
        idx = 0
        first_sign = 1
    result = deque()
    num = None
    while idx < len(text):
        if text[idx].isdigit():
            if num is None:
                num = 0
            num *= 10
            num += int(text[idx])
        else:
            if len(result) == 0:
                num *= first_sign
            result.append(num)
            num = None
            result.append(text[idx])
        idx += 1
    if len(result) == 0:
        num *= first_sign
    result.append(num)
    return result


def get(num1, operator, num2):
    result = num1
    if operator == '+':
        result += num2
    elif operator == '-':
        result -= num2
    elif operator == '*':
        result *= num2
    elif operator == '/':
        result = cpp_division(result, num2)
    return result


def cpp_division(dividend, divisor):
    if dividend * divisor < 0 and dividend % divisor != 0:
        return (dividend // divisor) + 1
    return dividend // divisor


def calculate(D):
    while len(D) > 1:
        if D[1] in MUL_DIV and D[-2] not in MUL_DIV:
            is_front = True
        elif D[1] not in MUL_DIV and D[-2] in MUL_DIV:
            is_front = False
        else:
            d1 = get(D[0], D[1], D[2])
            d2 = get(D[-3], D[-2], D[-1])
            if d1 >= d2:
                is_front = True
            else:
                is_front = False

        if is_front:
            n1 = D.popleft()
            n2 = D.popleft()
            n3 = D.popleft()
            d1 = get(n1, n2, n3)
            D.appendleft(d1)
        else:
            n3 = D.pop()
            n2 = D.pop()
            n1 = D.pop()
            d2 = get(n1, n2, n3)
            D.append(d2)
    print(D.pop())


if __name__ == '__main__':
    T = text_parser(input())
    calculate(T)
