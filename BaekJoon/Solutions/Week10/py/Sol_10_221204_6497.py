"""
https://www.acmicpc.net/problem/6497
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
    if px == py:
        return
    elif px < py:
        p[py] = px
    else:
        p[px] = py


if __name__ == '__main__':
    while True:
        m, n = map(int, input().split())
        if m == n == 0:
            break

        total_expense = 0
        edge_heap = []
        parents = [i for i in range(m)]
        for _ in range(n):
            x, y, z = map(int, input().split())
            total_expense += z
            heappush(edge_heap, (z, x, y))

        while edge_heap:
            pz, px, py = heappop(edge_heap)
            fpx, fpy = find(parents, px), find(parents, py)
            if fpx == fpy:
                continue

            union(parents, fpx, fpy)
            total_expense -= pz

        print(total_expense)