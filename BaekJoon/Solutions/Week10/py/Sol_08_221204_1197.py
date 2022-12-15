"""
https://www.acmicpc.net/problem/1197
"""
from heapq import heappush, heappop


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
    V, E = map(int, input().split())
    edge_heap = []
    vertices = [v for v in range(V+1)]
    weight_cnt = 0

    for _ in range(E):
        a, b, c = map(int, input().split())
        heappush(edge_heap, (c, a, b))

    while edge_heap:
        pc, pa, pb = heappop(edge_heap)
        if find(vertices, pa) == find(vertices, pb):
            continue

        weight_cnt += pc
        union(vertices, pa, pb)

    print(weight_cnt)