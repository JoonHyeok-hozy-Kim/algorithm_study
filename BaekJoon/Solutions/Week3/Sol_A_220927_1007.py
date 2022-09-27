"""
1007. 벡터 매칭
https://www.acmicpc.net/problem/1007
"""
from copy import deepcopy
from collections import deque
from math import inf


def get_length(vector):
    return pow(pow(vector[0], 2) + pow(vector[1], 2), .5)


def recursive_comb(points, i=0, x=0, y=0, pos_cnt=0, neg_cnt=0, min_val=None):

    if i == len(points):
        return get_length((x, y))

    if pos_cnt < len(points)//2:
        temp = recursive_comb(points, i+1, x+points[i][0], y+points[i][1], pos_cnt+1, neg_cnt)
        min_val = temp if min_val is None else min(min_val, temp)

    if neg_cnt < len(points)//2:
        temp = recursive_comb(points, i+1, x-points[i][0], y-points[i][1], pos_cnt, neg_cnt+1)
        min_val = temp if min_val is None else min(min_val, temp)

    return min_val


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        points = []
        for _ in range(N):
            points.append(list(map(int, input().split())))
        # print(points)
        print('{:.12f}'.format(recursive_comb(points)))



