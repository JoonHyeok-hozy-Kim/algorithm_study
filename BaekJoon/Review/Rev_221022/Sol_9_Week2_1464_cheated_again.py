"""
https://www.acmicpc.net/problem/1464
"""

from collections import deque


if __name__ == '__main__':
    text_list = list(input())
    # print(text_list)

    result = deque()
    result.append(text_list[0])

    for i in range(1, len(text_list)):
        if text_list[i] <= result[0]:
            result.appendleft(text_list[i])
        else:
            result.append(text_list[i])
    print(''.join(result))