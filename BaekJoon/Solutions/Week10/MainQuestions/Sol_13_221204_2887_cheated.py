"""
https://www.acmicpc.net/problem/2887
"""
from heapq import heappop, heappush


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


if __name__ == '__main__':
    N = int(input())
    planets = [None] * N
    for i in range(N):
        planets[i] = tuple(map(int, input().split()))

    K = []
    for j in range(3):
        planets.sort(key=lambda x: x[j])
        for k in range(N-1):
            heappush(K, (abs(planets[k+1][j]-planets[k][j]), planets[k+1], planets[k]))

    map_planet = {}
    for i in range(N):
        map_planet[planets[i]] = i
        planets[i] = i
    # print(planets)
    # print(map_planet)

    total_cost = 0
    while K:
        popped_cost, x, y = heappop(K)
        px, py = find(planets, map_planet[x]), find(planets, map_planet[y])
        if px == py:
            continue

        union(planets, px, py)
        total_cost += popped_cost
    print(total_cost)