"""
https://www.acmicpc.net/problem/1647
"""
from collections import deque
from heapq import heappop, heappush


def prim_jarnik(E, H):
    heap = [(0, 1)]
    total_length = 0
    max_length = 0
    while heap:
        popped_length, popped = heappop(heap)
        if H[popped]:
            continue

        H[popped] = True
        total_length += popped_length
        max_length = max(max_length, popped_length)
        for linked in E[popped]:
            if H[linked]:
                continue
            heappush(heap, (E[popped][linked], linked))

    return total_length - max_length


if __name__ == '__main__':
    N, M = map(int, input().split())
    edges = {}
    houses = [False] * (N+1)
    for _ in range(M):
        a, b, c = map(int, input().split())
        if a not in edges:
            edges[a] = {}
        edges[a][b] = c
        if b not in edges:
            edges[b] = {}
        edges[b][a] = c

    print(prim_jarnik(edges, houses))