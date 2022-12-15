"""
https://www.acmicpc.net/problem/10423
"""
from heapq import heappop, heappush


def find(p, x):
    if p[x] == x:
        return x
    p[x] = find(p, p[x])
    return p[x]


def union(p, x, y):
    if x == y:
        return x
    px, py = find(p, x), find(p, y)
    if px == py:
        return px
    elif px < py:
        p[py] = px
    else:
        p[px] = py
    return p[px]


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    parents = [i for i in range(N+1)]
    plant_link = [None] * (N+1)
    total_cost = 0

    for plant in map(int, input().split()):
        plant_link[plant] = plant

    edge_heap = []
    for _ in range(M):
        u, v, w = map(int, input().split())
        heappush(edge_heap, (w, u, v))

    while edge_heap:
        popped_cost, pu, pv = heappop(edge_heap)
        fpu, fpv = find(parents, pu), find(parents, pv)
        # print('\n pu : {} -> {}, pv : {} -> {}'.format(pu, fpu, pv, fpv))
        if fpu == fpv:
            continue

        if plant_link[fpu] is not None and plant_link[fpv] is not None:
            continue

        ppp = union(parents, fpu, fpv)
        total_cost += popped_cost

        if plant_link[fpu] is not None:
            plant_link[ppp] = plant_link[fpu]
        elif plant_link[fpv] is not None:
            plant_link[ppp] = plant_link[fpv]

        # print('plant_link_map : {}'.format(plant_link_map))
        # print('parents : {}'.format(parents))

    print(total_cost)