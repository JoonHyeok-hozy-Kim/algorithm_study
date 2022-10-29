"""
https://www.acmicpc.net/problem/15686
"""

from itertools import combinations
from copy import deepcopy


def calculate_chicken_distance(house, chicken):
    return abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])


if __name__ == '__main__':
    N, M = map(int, input().split())
    house_map = {}
    chicken_map = {}

    for i in range(N):
        j = 0
        for spot in map(int, input().split()):
            if spot == 1:
                house_map[(i, j)] = {}

            elif spot == 2:
                chicken_map[(i, j)] = {}

            j += 1

    for house in house_map:
        for chicken in chicken_map:
            distance = calculate_chicken_distance(house, chicken)
            house_map[house] = None
            chicken_map[chicken][house] = distance

    # print(house_map)
    # print(chicken_map)

    min_chicken_distance = None
    for chicken_list in combinations(chicken_map.keys(), M):
        H = deepcopy(house_map)
        for c in chicken_list:
            for h in chicken_map[c]:
                H[h] = min(H[h], chicken_map[c][h]) if H[h] is not None else chicken_map[c][h]

        dist_sum = 0
        for h in H:
            dist_sum += H[h]

        min_chicken_distance = min(min_chicken_distance, dist_sum) if min_chicken_distance is not None else dist_sum
        # print(dist_sum, min_chicken_distance, chicken_list)

    print(min_chicken_distance)
