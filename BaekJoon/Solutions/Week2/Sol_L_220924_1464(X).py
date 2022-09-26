"""
1464. 뒤집기 3
https://www.acmicpc.net/problem/1464
"""
from collections import deque
from copy import deepcopy

def partial_reverse(iterable, start, end):
    while start < end:
        iterable[start], iterable[end] = iterable[end], iterable[start]
        start += 1
        end -= 1


if __name__ == '__main__':
    L = list(input())
    # print(L)
    for i in range(len(L)-1):
        if L[i] > L[i+1] and L[0] >= L[i+1]:
            partial_reverse(L, 0, i)
            # print('R1({}) : {}'.format(i, L))
            if L[i] >= L[i+1]:
                partial_reverse(L, 0, i+1)
                # print('R1({}) : {}'.format(i+1, L))
        # print('{}-th : {}'.format(i, L))
    print(''.join(L))