"""
15686. 치킨 배달
https://www.acmicpc.net/problem/15686
"""
from copy import deepcopy
from itertools import combinations


def distance(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


def match_house_and_chicken(H, C, CM):
    for c in C:
        CM[c] = {}
        for h in H:
            CM[c][h] = distance(c, h)

    return CM


def get_city_chicken_distance(H, C, CM):
    D = 0
    for h in H:
        d = None
        for c in C:
            d = min(d, CM[c][h]) if d is not None else CM[c][h]
        D += d
    return D


def recursive_destroy(H, C, CM, m, cnt=0, min_dist=None):
    if len(C) == m:
        return get_city_chicken_distance(H, C, CM)

    n = len(C)
    for k in range(n):
        c_C = deepcopy(C)
        c_C.pop(k)
        temp_min_dist = recursive_destroy(H, c_C, CM, m, cnt+1, min_dist)
        min_dist = min(min_dist, temp_min_dist) if min_dist is not None else temp_min_dist

    return min_dist


def combination_sol(H, C, CM, m):
    min_dist = None
    combs = combinations(C, m)
    for cmb in combs:
        temp_dist = get_city_chicken_distance(H, cmb, CM)
        min_dist = min(min_dist, temp_dist) if min_dist is not None else temp_dist
    return min_dist



if __name__ == '__main__':
    N, M = map(int, input().split())
    city = []
    chickens = []
    houses = []
    chicken_map = {}
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            if row[j] == 1:
                houses.append((i, j))
            elif row[j] == 2:
                chickens.append((i, j))
        city.append(row)

    chicken_map = match_house_and_chicken(houses, chickens, chicken_map)
    # print(chicken_map)

    # result = recursive_destroy(houses, chickens, chicken_map, M)
    # print(result)

    result = combination_sol(houses, chickens, chicken_map, M)
    print(result)