"""
https://www.acmicpc.net/problem/1007
"""

from copy import deepcopy


def get_vector(p1, p2):
    return p1[0]-p2[0], p1[1]-p2[1]


def get_distance(x, y):
    return pow(pow(x, 2) + pow(y, 2), .5)


def recursive_trial(P, x=0, y=0, result=None):
    if len(P) == 0:
        print(x, y)
        return get_distance(x, y)

    p1 = P.pop()
    for i in range(len(P)):
        cP = deepcopy(P)
        p2 = cP.pop(i)
        v = get_vector(p1, p2)

        if get_distance(x+v[0], y+v[1]) < get_distance(x-v[0], y-v[1]):
            temp = recursive_trial(cP, x+v[0], y+v[1], result)
        else:
            temp = recursive_trial(cP, x-v[0], y-v[1], result)

        result = min(result, temp) if result is not None else temp

    return result


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        points = [list(map(int, input().split())) for _ in range(N)]
        # print(points)

        print(recursive_trial(points))
