"""
https://www.acmicpc.net/problem/2887
"""
from heapq import heappop, heappush
input = __import__('sys').stdin.readline


def calculate_tunnel_cost(a, b):
    return min(abs(a[0]-b[0]), abs(a[1]-b[1]), abs(a[2]-b[2]))


def find(p, x):
    if p[x] == x:
        return x
    p[x] = find(p, p[x])
    return p[x]


def union(p, x, y):
    if x == y:
        return
    px, py = find(p, x), find(p, y)
    p[py] = px


def prim_jarnik(N, PL, PA):
    total_cost = 0
    heap = []
    max_added_cost = 0
    for j in range(1, N):
        temp_cost = calculate_tunnel_cost(PL[0], PL[j])
        heappush(heap, (temp_cost, 0, j))
        max_added_cost = max(max_added_cost, temp_cost)

    while heap:
        popped_cost, pi, pj = heappop(heap)
        fpi, fpj = find(PA, pi), find(PA, pj)
        if fpi == fpj:
            continue

        ppp = union(PA, fpi, fpj)
        total_cost += popped_cost
        for k in range(N):
            if find(PA, k) != ppp:
                temp_cost = calculate_tunnel_cost(PL[k], PL[pj])
                if len(heap) < N:
                    heappush(heap, (temp_cost, k, pj))
                elif temp_cost < max_added_cost:
                    heappush(heap, (temp_cost, k, pj))
                    max_added_cost = max(max_added_cost, temp_cost)

    return total_cost



if __name__ == '__main__':
    N = int(input())
    planets = [None] * N
    parents = [i for i in range(N)]
    for i in range(N):
        planets[i] = tuple(map(int, input().split()))
    # print(planet_map)
    # print(parents)

    print(prim_jarnik(N, planets, parents))