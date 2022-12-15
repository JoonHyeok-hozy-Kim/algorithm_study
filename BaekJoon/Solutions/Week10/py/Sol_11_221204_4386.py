"""
https://www.acmicpc.net/problem/4386
"""
from heapq import heappop, heappush


def get_distance(a, b):
    temp = (a[0] - b[0]) ** 2
    temp += (a[1] - b[1]) ** 2
    return temp ** .5


def prim_jarnik(M, L, s):
    heap = [(0, s)]
    total_length = 0
    while heap:
        popped_distance, popped = heappop(heap)
        if L[M[popped]]:
            continue

        L[M[popped]] = True
        total_length += popped_distance
        for linked in M:
            if L[M[linked]]:
                continue
            heappush(heap, (get_distance(popped, linked), linked))

    return total_length


if __name__ == '__main__':
    N = int(input())
    star_map = {}
    star_list = [None] * N
    id = 0
    starting_star = None

    for _ in range(N):
        (x, y) = map(float, input().split())
        if (x, y) not in star_map:
            star_map[(x, y)] = id
            star_list[id] = False
            id += 1
        starting_star = (x, y)

    # print('star_map : {}'.format(star_map))
    # print('star_list : {}'.format(star_list))

    print(prim_jarnik(star_map, star_list, starting_star))