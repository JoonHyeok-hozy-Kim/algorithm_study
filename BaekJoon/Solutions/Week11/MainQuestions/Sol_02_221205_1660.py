"""
https://www.acmicpc.net/problem/1660
"""
from bisect import bisect_left
from math import inf


def create_tetrahedrons(K):
    size = 0
    cnt = 1
    result = []
    while size < K:
        size += cnt*(cnt+1)/2
        result.append(size)
        cnt += 1
    return result


if __name__ == '__main__':
    N = int(input())
    T = create_tetrahedrons(N)
    print('T : {}'.format(T))
    min_cnt = inf
    for t in reversed(range(len(T))):
        if T[t] > N:
            continue
        new = N
        x = t
        temp_cnt = 0
        while new > 0 and temp_cnt < min_cnt:
            temp_cnt += new // T[x]
            temp = new % T[x]
            x = bisect_left(T, )